class Radar {
            constructor(canvasId, options = {}) {
                this.canvas = document.getElementById(canvasId);
                this.ctx = this.canvas.getContext('2d');
                this.width = this.canvas.width = options.width || 600;
                this.height = this.canvas.height = options.height || 600;
                this.centerX = this.width / 2;
                this.centerY = this.height / 2;
                this.radius = Math.min(this.width, this.height) / 2 - 20;
                this.color = options.color || '#0adb1f';
                this.backgroundColor = options.backgroundColor || '#000';
                this.numCircles = options.circles || 4;
                this.numCrosshairs = options.crosshairs || 8;
                this.objects = [];
                this.updateInterval = options.updateInterval || 1000; // ms
                this.running = false;
                
                this.draw();
            }

            start() {
                if (!this.running) {
                    this.running = true;
                    this.intervalId = setInterval(() => this.updatePositions(), this.updateInterval);
                }
            }

            stop() {
                if (this.running) {
                    this.running = false;
                    clearInterval(this.intervalId);
                }
            }

            updatePositions() {
                this.objects.forEach(obj => {
                    // Convert velocity angle to radians (compass style: 0 = up)
                    const velocityRadians = (obj.velocity.angle - 90) * (Math.PI / 180);
                    
                    // Calculate change in distance and angle based on velocity
                    const deltaDistance = (obj.velocity.magnitude / 100) * (this.radius / this.numCircles);
                    const deltaX = Math.cos(velocityRadians) * deltaDistance;
                    const deltaY = Math.sin(velocityRadians) * deltaDistance;
                    
                    // Convert current angle/distance to cartesian
                    const currentRadians = (obj.angle - 90) * (Math.PI / 180);
                    let x = Math.cos(currentRadians) * obj.distance * this.radius + deltaX;
                    let y = Math.sin(currentRadians) * obj.distance * this.radius + deltaY;
                    
                    // Convert back to polar coordinates
                    const newDistance = Math.sqrt(x * x + y * y) / this.radius;
                    let newAngle = (Math.atan2(y, x) * (180 / Math.PI)) + 90;
                    
                    // Normalize angle
                    newAngle = ((newAngle % 360) + 360) % 360;
                    
                    // Wrap around if beyond radar range
                    if (newDistance > 1) {
                        obj.distance = newDistance - 1;
                    } else if (newDistance < 0) {
                        obj.distance = 1 + newDistance;
                    } else {
                        obj.distance = newDistance;
                    }
                    
                    obj.angle = newAngle;
                });
                
                this.draw();
            }

            draw() {
                this.drawBackground();
                this.drawCircles();
                this.drawCrosshairs();
                this.drawObjects();
            }

            drawBackground() {
                this.ctx.fillStyle = this.backgroundColor;
                this.ctx.fillRect(0, 0, this.width, this.height);
            }

            drawCircles() {
                this.ctx.strokeStyle = this.color;
                this.ctx.lineWidth = 1;
                this.ctx.globalAlpha = 0.6;

                for (let i = 1; i <= this.numCircles; i++) {
                    const r = (this.radius / this.numCircles) * i;
                    this.ctx.beginPath();
                    this.ctx.arc(this.centerX, this.centerY, r, 0, Math.PI * 2);
                    this.ctx.stroke();
                }

                this.ctx.globalAlpha = 1;
            }

            drawCrosshairs() {
                this.ctx.strokeStyle = this.color;
                this.ctx.lineWidth = 1;
                this.ctx.globalAlpha = 0.6;
                const angleStep = (Math.PI * 2) / this.numCrosshairs;

                for (let i = 0; i < this.numCrosshairs; i++) {
                    const angle = angleStep * i;
                    const x = this.centerX + Math.cos(angle) * this.radius;
                    const y = this.centerY + Math.sin(angle) * this.radius;

                    this.ctx.beginPath();
                    this.ctx.moveTo(this.centerX, this.centerY);
                    this.ctx.lineTo(x, y);
                    this.ctx.stroke();
                }

                this.ctx.globalAlpha = 1;
            }

            drawObjects() {
                this.objects.forEach(obj => {
                    // Convert angle from compass degrees (0 = up) to standard math (0 = right)
                    const radians = (obj.angle - 90) * (Math.PI / 180);
                    const distance = Math.min(obj.distance, 1);
                    const x = this.centerX + Math.cos(radians) * (this.radius * distance);
                    const y = this.centerY + Math.sin(radians) * (this.radius * distance);

                    // Draw velocity vector
                    this.drawVelocityVector(x, y, obj.velocity);

                    // Draw icon
                    this.ctx.fillStyle = this.color;
                    this.ctx.font = obj.size || '20px Arial';
                    this.ctx.textAlign = 'center';
                    this.ctx.textBaseline = 'middle';
                    this.ctx.fillText(obj.icon, x, y);

                    // Draw label if provided
                    if (obj.label) {
                        this.ctx.font = '12px Arial';
                        this.ctx.fillText(obj.label, x, y + 18);
                    }
                });
            }

            drawVelocityVector(x, y, velocity) {
                const vectorRadians = (velocity.angle - 90) * (Math.PI / 180);
                const vectorLength = velocity.magnitude * 1.5;
                const endX = x + Math.cos(vectorRadians) * vectorLength;
                const endY = y + Math.sin(vectorRadians) * vectorLength;

                this.ctx.strokeStyle = this.color;
                this.ctx.lineWidth = 1;
                this.ctx.globalAlpha = 0.5;
                this.ctx.beginPath();
                this.ctx.moveTo(x, y);
                this.ctx.lineTo(endX, endY);
                this.ctx.stroke();

                // Draw arrowhead
                const arrowSize = 6;
                const angle1 = vectorRadians - (Math.PI * 0.3);
                const angle2 = vectorRadians + (Math.PI * 0.3);
                this.ctx.beginPath();
                this.ctx.moveTo(endX, endY);
                this.ctx.lineTo(endX + Math.cos(angle1) * arrowSize, endY + Math.sin(angle1) * arrowSize);
                this.ctx.moveTo(endX, endY);
                this.ctx.lineTo(endX + Math.cos(angle2) * arrowSize, endY + Math.sin(angle2) * arrowSize);
                this.ctx.stroke();

                this.ctx.globalAlpha = 1;
            }

            addObject(obj) {
                if (obj.angle === undefined || obj.distance === undefined || !obj.icon || !obj.velocity) {
                    console.error('Object must have: angle, distance, icon, and velocity properties');
                    console.error('Velocity format: { magnitude: number, angle: number }');
                    return;
                }
                this.objects.push(obj);
                this.draw();
            }

            clearObjects() {
                this.objects = [];
                this.draw();
            }

            removeObject(index) {
                this.objects.splice(index, 1);
                this.draw();
            }

            updateObject(index, updates) {
                if (this.objects[index]) {
                    Object.assign(this.objects[index], updates);
                    this.draw();
                }
            }

            getObjects() {
                return this.objects;
            }
        }

        // Initialize radar
        const radar = new Radar('radar', {
            width: 600,
            height: 600,
            color: '#0adb1f',
            backgroundColor: '#000',
            circles: 4,
            crosshairs: 8,
            updateInterval: 1000 // Update every second
        });

        // Example: Add objects with velocity
        radar.addObject({
            icon: '▲',
            angle: 0,
            distance: 0.3,
            label: 'Target 1',
            size: '24px',
            velocity: {
                magnitude: 8,  // Speed (relative to radar)
                angle: 45      // Direction in degrees (0 = north)
            }
        });

        radar.addObject({
            icon: '●',
            angle: 90,
            distance: 0.6,
            label: 'Target 2',
            velocity: {
                magnitude: 5,
                angle: 180
            }
        });

        radar.addObject({
            icon: '■',
            angle: 180,
            distance: 0.2,
            label: 'Target 3',
            velocity: {
                magnitude: 12,
                angle: 270
            }
        });

        radar.addObject({
            icon: '♦',
            angle: 270,
            distance: 0.5,
            label: 'Target 4',
            velocity: {
                magnitude: 6,
                angle: 90
            }
        });

        // Start the radar
        radar.start();

        // Update info display
        function updateInfo() {
            const infoDiv = document.getElementById('info');
            const objects = radar.getObjects();
            let html = '<strong>Object Positions & Velocities (Updated Every Second)</strong>';
            objects.forEach((obj, i) => {
                html += `<div class="object-info">
                    <strong>${obj.label}</strong> - 
                    Angle: ${obj.angle.toFixed(1)}° | 
                    Distance: ${(obj.distance * 100).toFixed(1)}% | 
                    Velocity: ${obj.velocity.magnitude} @ ${obj.velocity.angle}°
                </div>`;
            });
            infoDiv.innerHTML = html;
        }

        // Update info display every update
        setInterval(updateInfo, 1000);
        updateInfo();
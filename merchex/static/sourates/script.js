gsap.fromTo(".haut img", {y: 60, opacity: 0}, {y: 0, duration: 1.5, opacity: 1});
gsap.fromTo("h1", {y: -60, opacity: 0}, {y: 0, duration: 1.5, opacity: 1});
gsap.fromTo(".sourate h3, .sourate p, .B h5", {x: -60, opacity: 0}, {x: 0, duration: 1.5, opacity: 1, stagger: { each : 0.4}});
gsap.fromTo(".info p", {opacity: 0}, {opacity: 1, duration: 1.5});
gsap.fromTo(".conditions", {opacity: 0}, {opacity: 1, duration: 1.5, stagger: { each : 0.4}});
gsap.fromTo(".middle img", {x: -60, opacity: 0}, {x: 0, duration: 2.5, opacity: 1, stagger: { each : 0.4}});
gsap.fromTo(".middle2 img", {x: 60, opacity: 0}, {x: 0, duration: 2.5, opacity: 1, stagger: { each : 0.4}});
// Khởi tạo Swiper
var swiper = new Swiper(".swiper", {
    effect: "slide", // Hiệu ứng chuyển slide
    speed: 900, // Tốc độ chuyển đổi slide
    loop: true, // Vòng lặp vô hạn
    mousewheel: {
        invert: false, // Không đảo chiều cuộn chuột
        thresholdDelta: 50, // Ngưỡng thay đổi để kích hoạt cuộn
        sensitivity: 1, // Độ nhạy của cuộn chuột
    },
});

// Khởi tạo particles.js
particlesJS("particles-js", {
    particles: {
        number: {
            value: 200, // Số lượng particles
            density: {
                enable: true, // Bật tính năng density
                value_area: 800, // Mật độ particles trên diện tích
            },
        },
        color: {
            value: "#f0c394", // Màu sắc của particles
        },
        opacity: {
            value: 0.4, // Độ mờ của particles
            random: false, // Không ngẫu nhiên độ mờ
            anim: {
                enable: false, // Tắt animation cho opacity
                speed: 1, // Tốc độ animation của opacity
                opacity_min: 0.1, // Độ mờ tối thiểu
                sync: false, // Không đồng bộ animation
            },
        },
        size: {
            value: 3, // Kích thước của particles
            random: true, // Kích thước ngẫu nhiên
            anim: {
                enable: false, // Tắt animation cho kích thước
                speed: 40, // Tốc độ animation của kích thước
                size_min: 0.1, // Kích thước tối thiểu
                sync: false, // Không đồng bộ animation
            },
        },
        line_linked: {
            enable: true, // Bật tính năng liên kết giữa các particles
            distance: 150, // Khoảng cách liên kết giữa các particles
            color: "#f0c394", // Màu sắc của đường liên kết
            opacity: 0.4, // Độ mờ của đường liên kết
            width: 1, // Độ rộng của đường liên kết
        },
        move: {
            enable: true, // Bật tính năng di chuyển của particles
            speed: 0.5, // Tốc độ di chuyển của particles
            direction: "none", // Hướng di chuyển (none để ngẫu nhiên)
            random: false, // Không di chuyển ngẫu nhiên
            straight: false, // Không di chuyển thẳng
            out_mode: "out", // Chế độ di chuyển ra ngoài
            bounce: false, // Không bật lại khi va chạm
            attract: {
                enable: false, // Tắt tính năng hút nhau của particles
                rotateX: 600, // Trục X để hút
                rotateY: 1200, // Trục Y để hút
            },
        },
    },
    retina_detect: true, // Bật tính năng nhận diện màn hình retina
});
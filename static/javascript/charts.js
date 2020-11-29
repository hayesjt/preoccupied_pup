// ENTIRE FILE FOR GRAPHS SHOWN ON DASHBOARD
'use strict';

// MEAL PIE CHART
$.get('/mealdata', (res) => {
    var MealData = res;

    var meal = document.getElementById('mealChart').getContext('2d');
    var mealChart = new Chart(meal, {
        // The type of chart we want to create
        type: 'pie',
        data: {
            labels: ['Breakfast', 'Lunch', 'Dinner', 'Snack', 'Treat', 'Bone'],
            datasets: [{
                label: "Population (millions)",
                backgroundColor: ["#6D696A", "#5EB1BF", "#D3D3D3", "#EF7B45", "#CDEDF6", "#F14304"],
                data: MealData
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Monthly Meal Data'
            },
        }
    });

});

// MOOD BAR CHART
$.get('/mooddata', (res) => {
    var MoodData = res;

    var mood = document.getElementById('moodChart').getContext('2d');
    var moodChart = new Chart(mood, {
        type: 'bar',
        data: {
            labels: ["Happy", "Sad", "Anxious", "Lonely", "Energetic", "Aggressive"],
            datasets: [
                {
                    backgroundColor: ["#F14304", "#5EB1BF", "#D3D3D3", "#EF7B45", "#CDEDF6", "#6D696A"],
                    data: MoodData
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            legend: { display: false },
            title: {
                display: true,
                text: 'Monthly Mood Data'
            },
        }
    });
});

// GROOM HORIZONTAL BAR GRAPH
$.get('/groomdata', (res) => {
    var GroomData = res;

    var groom = document.getElementById('groomChart').getContext('2d');
    var moodChart = new Chart(groom, {
        type: 'bar',
        data: {
            labels: ["Brushed", "Clipped Nails", "Bath", "Hair Cut", "Teeth Brushed", "Ears Cleaned"],
            datasets: [
                {
                    backgroundColor: ["#F14304", "#5EB1BF", "#D3D3D3", "#EF7B45", "#CDEDF6", "#6D696A"],
                    data: GroomData
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            legend: { display: false },
            title: {
                display: true,
                text: 'Monthly Grooming Data'
            }
        }
    });
});

// TRAINING BAR GRAPH
$.get('/trainingdata', (res) => {
    var TrainData = res;

    var train = document.getElementById('trainChart').getContext('2d');
    var moodChart = new Chart(train, {
        type: 'bar',
        data: {
            labels: ["Sit", "Place", "Lay Down", "Touch", "Heel", "High Five"],
            datasets: [
                {
                    backgroundColor: ["#F14304", "#5EB1BF", "#D3D3D3", "#EF7B45", "#CDEDF6", "#6D696A"],
                    data: TrainData
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            legend: { display: false },
            title: {
                display: true,
                text: 'Monthly Training Data'
            }
        }
    });
});

// ACTIVITY BAR GRAPH
$.get('/activitydata', (res) => {
    var ActivityData = res;
    console.log(ActivityData)

    var train = document.getElementById('activityChart').getContext('2d');
    var moodChart = new Chart(train, {
        type: 'bar',
        data: {
            labels: ["Dog Park", "Long Walk", "Short Walk", "Puppy Play Date", "Play Ball/Frisbee", "Run"],
            datasets: [
                {
                    backgroundColor: ["#F14304", "#5EB1BF", "#D3D3D3", "#EF7B45", "#CDEDF6", "#6D696A"],
                    data: ActivityData

                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            legend: { display: false },
            title: {
                display: true,
                text: 'Monthly Activity Data'
            }
        }
    });
});

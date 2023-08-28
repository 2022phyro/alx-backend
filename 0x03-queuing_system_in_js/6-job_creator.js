const kue = require('kue');
const queue = kue.createQueue();

// Define the job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message.',
};

// Create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData);

// Event handler for successful job creation
job.on('created', (id) => {
  console.log(`Notification job created: ${id}`);
});

// Event handler for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event handler for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save((error) => {
  if (error) {
    console.error('Error creating job:', error);
  } else {
    console.log('Job saved to the queue.');
  }

  // Close the Kue queue connection
  queue.shutdown(500, (err) => {
    console.log('Kue queue shut down.');
    process.exit(0);
  });
});


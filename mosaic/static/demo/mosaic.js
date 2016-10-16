(function () {
  var data = [{"first_name": "Dr. Mario", "last_name": "Jimenez ", "lastChildVisit": "2012-07-20 00:00:00", "tags": "", "childVisitFrequency": 0, "ip": "2602:306:c5f6:9400:d1f7:9ea:87fe:5eda", "related_submission": "", "numChildren": 2, "courtCity": "Miami ", "homeCity": "Miami ", "other": "", "courtCosts": 75000, "relation": "erased_dad", "courtCountry": "US", "homeCountry": "US", "time": "2016-10-16 04:05:43", "url": "20161015_205018.mp4", "email": "Marioaj01@yahoo.com", "milestones": "All Holy days, birthdays for over 4 years"}, {"first_name": "Chris ", "last_name": "Strickland ", "lastChildVisit": "2016-10-14 00:00:00", "tags": "", "childVisitFrequency": 0, "ip": "2602:306:cd75:94b0:f58f:7f09:6dff:6ee7", "related_submission": "", "numChildren": 2, "courtCity": "Brandon/Rankin County ", "homeCity": "Pearl", "other": "", "courtCosts": 5000, "relation": "erased_mom", "courtCountry": "US", "homeCountry": "US", "time": "2016-10-16 16:02:54", "url": "tmp_30485-videocompress-091-20161016_091251-479493870.mp4", "email": "allaboutmyboys0011@gmail.com", "milestones": "missing the first day of school with my 5 year old son and missing my 16 year son play high school football"}, {"first_name": "Dave", "last_name": "Slotter", "lastChildVisit": "2014-06-14 00:00:00", "tags": "", "childVisitFrequency": 0, "ip": "63.116.20.2", "related_submission": "", "numChildren": 2, "courtCity": "McKinney", "homeCity": "Plano", "other": "", "courtCosts": 75000, "relation": "erased_dad", "courtCountry": "US", "homeCountry": "US", "time": "2016-10-16 17:11:55", "url": "2016-10-16_-_Slotter_David_ErasedDad.mp4", "email": "alienated.dad.tx@gmail.com", "milestones": "High School Graduation"}, {"first_name": "Michael", "last_name": "Gilligan", "lastChildVisit": "2014-10-10 00:00:00", "tags": "", "childVisitFrequency": 0, "ip": "67.82.234.28", "related_submission": "", "numChildren": 2, "courtCity": "Central Islip", "homeCity": "Deer Park", "other": "", "courtCosts": 60000, "relation": "erased_dad", "courtCountry": "US", "homeCountry": "US", "time": "2016-10-16 17:12:53", "url": "2016.10.16._erased_dad.mp4", "email": "mikegilligan2@gmail.com", "milestones": "Birthdays"}, {"first_name": "Brenda", "last_name": "Cimakasky", "lastChildVisit": "2011-11-25 00:00:00", "tags": "", "childVisitFrequency": 0, "ip": "104.228.69.142", "related_submission": "", "numChildren": 1, "courtCity": "Lyons", "homeCity": "Elmira", "other": "", "courtCosts": 2000000, "relation": "erased_mom", "courtCountry": "US", "homeCountry": "US", "time": "2016-10-16 18:23:09", "url": "VID_20161016_130254.mp4", "email": "bjcfirebrand@epix.net", "milestones": "Everything"}, {"first_name": "Keeley", "last_name": "Petersen ", "lastChildVisit": "2013-04-12 00:00:00", "tags": "", "childVisitFrequency": 0, "ip": "2602:306:c43f:2da0:a4b1:a90d:53e6:ef39", "related_submission": "", "numChildren": 4, "courtCity": "St George ", "homeCity": "Lemoore ", "other": "", "courtCosts": 20000, "relation": "erased_sister", "courtCountry": "US", "homeCountry": "US", "time": "2016-10-16 18:51:41", "url": "20161016_094347.mp4", "email": "Kimblue8@hotmail.com", "milestones": ""}, {"first_name": "Jeffrey", "last_name": "Morgan", "lastChildVisit": "2015-05-05 00:00:00", "tags": "", "childVisitFrequency": 0, "ip": "2602:30a:c0b8:3240:b404:40c7:7666:9eb6", "related_submission": "", "numChildren": 2, "courtCity": "Dallas", "homeCity": "Dallas", "other": "", "courtCosts": 17, "relation": "erased_grandparent", "courtCountry": "US", "homeCountry": "US", "time": "2016-10-16 18:55:29", "url": "ErasingGrandparent.mp4", "email": "jeffintexas@gmail.com", "milestones": "Birthdays"}, {"first_name": "Malia ", "last_name": "Petersen ", "lastChildVisit": "2013-04-12 00:00: ", "tags": "", "childVisitFrequency": 0, "ip": "2602:306:c43f:2da0:a4b1:a90d:53e6:ef39", "related_submission": "", "numChildren": 4, "courtCity": "St. George ", "homeCity": "Lemoore ", "other": "", "courtCosts": 20000, "relation": "erased_sister", "courtCountry": "US", "homeCountry": "US", "time": "2016-10-16 19:32:13", "url": "20161016_095253.mp4", "email": "Kimblue8@hotmail.com", "milestones": ""},
  {url: 'IMG_3294.mov'},
  {url: 'Película del día 16-10-16 a la(s) 13.02.mov'}
]
  // console.log(data);
  var opts = {
    itemSelector: '.mosaic-item',
    columnWidth: '.mosaic-sizer',
  };

  var grid = document.getElementById('mosaic');

  for (var i = 0; i < data.length; ++i){
    var child = document.createElement('img');
    var childOpts = data[i];

    // child.style.height = childOpts.height;
    // child.style.width = childOpts.width;
    child.src = "static/demo/screen_grabs/" + childOpts.url + ".jpg";
    console.log(child.src)

    var lastVisit = new Date(childOpts.lastChildVisit);
    // console.log(lastVisit);
    var diff = new Date(Date.now() - lastVisit.getTime());
    // console.log(diff);
    var yrs = diff.getUTCFullYear() - 1970;
    var mnths = diff.getUTCMonth();

    var newTitle = "";

    if (yrs) {
      newTitle += yrs.toString() + " years";
    }

    if (mnths) {
      if (yrs) {
        newTitle += ", ";
      }
      newTitle += mnths.toString() + " months";
    }
    child.title = newTitle;

    child.className += ' mosaic-item';
    child.style.height='auto';
    child.style.width = '150px';

    child.setAttribute('data-rel', 'tooltip');

    grid.appendChild(child);

  }

  $('[data-rel="tooltip"]').tooltip();

  var mosaic = $("#mosiac").masonry(opts);

  // $(document).tooltip();

})();

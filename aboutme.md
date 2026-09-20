---
layout: default
title: "About · Children's Privacy & Youth AI Safety"
share-description: "Jake Chanenson is a CS PhD researcher at the University of Chicago and a Siebel Scholar who studies how to protect young people's privacy and safety, from K-12 EdTech to AI. Master of Legal Studies, UChicago Law."
---

<div class="page-content">
  <div class="page-inner">

    <div class="page-header">
      <h1 class="page-title">About Me</h1>
      <p class="page-subtitle" data-copy="ABOUT-SUBTITLE">Children's Privacy Scholar &middot; Youth AI Safety &middot; University of Chicago</p>
    </div>

<div class="about-body">
      
      <style>
        /* Mobile-first base styles */
        .about-intro-layout {
          display: flex;
          flex-direction: column-reverse; /* Puts the image on top of the text on mobile */
          gap: 2rem;
          align-items: center;
          margin-bottom: 2rem;
        }

        .about-intro-text {
          flex: 1 1 auto;
        }

        .about-intro-image {
          flex: 0 0 auto;
          width: 100%;
          max-width: 260px; /* Prevents the image from getting massive on phones */
        }

        .about-intro-image img {
          width: 100%;
          border-radius: 8px;
          box-shadow: 0 4px 12px rgba(0,0,0,0.1);
          display: block;
          object-fit: cover;
        }

        /* Desktop override */
        @media (min-width: 768px) {
          .about-intro-layout {
            flex-direction: row; /* Puts text on left, image on right */
            align-items: flex-start;
            gap: 3rem;
          }
          
          .about-intro-image {
            flex: 0 0 260px; /* Locks the image width on desktop */
          }
        }
      </style>

      <div class="about-intro-layout">
        
        <div class="about-intro-text">
          <p style="margin-top: 0;" data-copy="ABOUT-INTRO-1">
            I study how to protect <strong>young people's privacy and safety</strong> in technologies they are
            required to use and those they choose for themselves. I'm a CS PhD researcher at the University of
            Chicago, working with <a href="https://www.marshini.net/">Marshini Chetty</a> at the <a
            href="https://airlab.cs.uchicago.edu/">Amyoli Internet Research Lab</a>. My research began with
            schools, where institutions make technology decisions on students' behalf, and now examines how these
            responsibilities change as young people use AI for schoolwork and personal support. I combine
            human-computer interaction, computational methods, and legal analysis to guide the design and
            governance of these systems.
          </p>
          <p data-copy="ABOUT-INTRO-2">
            Children's privacy is where my work started and what connects it. In K&ndash;12 schools I studied who
            collects data about students, under what terms, and what oversight exists. These questions become
            harder to answer when students use AI tools that no adult at their school selected or reviewed, whether
            for homework or for something personal. My current work asks what students
            expect to happen to that information, how schools write rules for AI, and when teens trust AI for
            safety advice at all. I also organize a <a href="/ai-safety">workshop series on youth AI safety</a> at
            ACM CHI and ASSETS.
          </p>
        </div>

        <div class="about-intro-image">
          <img src="/assets/img/jake_headshot.jpeg" alt="Jake Chanenson headshot">
        </div>
        
      </div>

      <p data-copy="ABOUT-CREDENTIALS">
        I hold a <strong>Master of Legal Studies</strong> from the University of Chicago Law School, with a
        focus on privacy, copyright, and administrative law. That background shapes how I frame research
        questions about what legal protections require and how they work in practice. I am a <strong>Siebel
        Scholar</strong> (Class of 2027). My research has been published at <strong>ACM CHI, ACM FAccT, and
        PETS</strong>, and presented at venues including the Privacy Law Scholars Conference (PLSC). I am also an
        affiliate at <a href="https://citap.unc.edu/">UNC's Center for Information, Technology, and Public Life
        (CITAP)</a>.
      </p>
      <p data-copy="ABOUT-CLOSING">
        I am expecting to finish my PhD in spring 2027. My work sits at the intersection of research,
        law, and policy, and I am interested in positions across <strong>academia, industry, and government</strong>
        where that combination is an asset.
        If you are working on children's privacy, youth AI safety, or AI governance for minors,
        I would love to <a href="mailto:jchanen1@uchicago.edu">hear from you</a>.
      </p>


    <div class="about-stats">
      <div class="about-stat">
        <span class="about-stat-num">ACM CHI</span>
        <span class="about-stat-label">'23 HM &middot; '26 paper &amp; workshop</span>
      </div>
      <div class="about-stat">
        <span class="about-stat-num">FAccT '26</span>
        <span class="about-stat-label">ChatGPT governance in schools</span>
      </div>
      <div class="about-stat">
        <span class="about-stat-num">PETS '25</span>
        <span class="about-stat-label">LLMs + privacy policies</span>
      </div>
      <div class="about-stat">
        <span class="about-stat-num">CHI + ASSETS</span>
        <span class="about-stat-label">Youth AI safety workshop organizer</span>
      </div>
      <div class="about-stat">
        <span class="about-stat-num">Siebel Scholar</span>
        <span class="about-stat-label">Class of 2027</span>
      </div>
      <div class="about-stat">
        <span class="about-stat-num">Google</span>
        <span class="about-stat-label">Research intern '24&ndash;'25</span>
      </div>
    </div>


      <div class="about-links">
        <a href="/CV" class="btn btn-outline-accent">Abbreviated CV &rarr;</a>
        <a href="/research" class="btn btn-outline">Research</a>
        <a href="mailto:jchanen1@uchicago.edu" class="btn btn-outline">Email me</a>
      </div>
    </div>

{% include shared-cta.html %}

    <div class="about-site-section">
      <h2 class="about-site-heading">About This Site</h2>

      <p>
        This site started as a <a href="https://beautifuljekyll.com/">Beautiful Jekyll</a> theme and has since
        been substantially redesigned. The layout, typography, color system, and component styling are all
        custom-built. Beautiful Jekyll now serves only as a historical starting point, with none of its
        original CSS, JavaScript, or layout templates remaining in the final site.
      </p>

      <p>
        The redesign was built around a dark navy palette with serif display type
        (<a href="https://fonts.google.com/specimen/Libre+Baskerville">Libre Baskerville</a>),
        sans-serif body text (<a href="https://fonts.google.com/specimen/DM+Sans">DM Sans</a>),
        and a gold accent system. No Bootstrap. No jQuery. No analytics.
      </p>

      <h3 class="about-site-subheading">Built with</h3>
      <ul class="about-site-list">
        <li><a href="http://jekyllrb.com/">Jekyll</a> &mdash; static site generator</li>
        <li><a href="https://beautifuljekyll.com/">Beautiful Jekyll</a> &mdash; original theme scaffold (since replaced)</li>
        <li><a href="http://type-scale.com/">Type Scale</a> &mdash; typographic scale reference</li>
        <li><a href="https://github.com/liip/TheA11yMachine">The A11Y Machine</a> &mdash; accessibility auditing</li>
      </ul>

      <h3 class="about-site-subheading">Accessibility</h3>
      <p>
        This site targets WCAG 2.0 AA compliance. Color contrast ratios for body text and interactive elements
        meet or exceed the 4.5:1 minimum. If you encounter an accessibility issue, please
        <a href="mailto:jchanen1@uchicago.edu">let me know</a>.
      </p>
    </div>

  </div>
</div>
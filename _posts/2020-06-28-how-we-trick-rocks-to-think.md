---
layout: post
title: How We Trick Rocks to Think
subtitle: A layperson’s guide
css: /assets/css/blockquote_no_quote.css
tags: [cpu, tech explained, systems]
---

There is an excellent tuple of tweets by @daisyowl that go something like this:
> a CPU is literally a rock that we tricked into thinking

-(@daisyowl, 3/4/17)

> not to oversimplify: first you have to flatten the rock and put lightning inside it 

 -(@daisyowl, 3/4/17) 



I would go even further and add:

> a word of caution: if the rock thinks too hard it will become hot enough to boil water 

-(@Me, 6/17/20)


There are a lot of thinking rocks in use today. You use a thinking rock to write a text, browse the internet, and play music. Most people you know probably have at least one or two thinking rocks in their possession. A cursory count puts the number of these rocks thinking on a daily basis north of a billion! With so many thinking rocks around, perhaps you’ve idly wondered how exactly a flattened rock stuffed chockfull of lightning gets made. If so, you're in luck! Today we're going to explore how the thinking rocks that power your computer are created.

 

### What is a thinking rock exactly 

At its most basic level, a thinking rock is comprised of switches – called transistors – and wires that connect these switches together. These switches are combined in clever ways that, when powered by the aforementioned lightning (electricity), allow the rock to remember small amounts of information and to do addition. 

As a quick refresher, recall 

- multiplication is just adding the same number multiple times
  - $$4*x = x+x+x+x$$
- subtraction is adding a negative number to a positive 
  - $$x-y = x+(-y)$$
- division is the count of subtracting the same number multiple times
  - $$15/3 = 5$$ 
  - $$15-3-3-3-3-3 = 0$$ count of $$(-3)$$ is $$5$$

Modern thinking rocks have fancy tricks to make these and other more advanced mathematical operations go faster, but essentially all a thinking rock does is very speedy addition all day.

 

### A short aside on size and the thinking rock

Depending on the device you’re reading this post on, your thinking rock has around one to two billion (or more) transistors stuffed inside it.

Numbers at this magnitude are really hard to fathom. The semantics of saying “two billion” obfuscates the magnitude of the number. Written out, two billion is `2,000,000,000` -- even after writing out all nine of those zeros, the concept is still abstract. So, let’s make it a little more tangible. 

If I were to assemble a stack of two billion pieces of the thinnest printer paper I could find, the resulting tower reaches 50 kilometers or 31.07 miles into the air. That’s 4.3 times taller than the maximum height commercial planes fly at. It’s quite literally halfway to space! Put another way, you could stack 5 and a half Mt. Everests on top of each other, and it still wouldn’t be as tall as this stack of paper! 

I want to stress that this printer paper is the thinnest stuff that you can buy. If I stacked 100 pieces of this paper, the resulting pile would only be 5 centimeters or 1.97 inches tall. With that in mind, the fact that this same paper stacked two billion times is taller than 112 Empire State Buildings stacked on top of each other should hopefully drive home the magnitude of two billion. 

So, how do you stuff two billion transistors inside a square that fits in the palm of your hand? The answer is pretty obvious: to stuff an unfathomable number of objects into a small space, you just make the objects in question unfathomably small. Let me tell you, these transistors are veeery small. 

In 2014 you could buy a thinking rock packed full of transistors that were 400 silicon atoms (~80 nanometers) long. At this size, you couldn’t actually see them with an optical microscope! Incredibly, the size of the transistors in the most modern thinking rocks has gotten even smaller. 



### How do we create a thinking rock 

This itty bitty size, while impressive, makes the creation of a thinking rock (known as a CPU) all the more mysterious. Given how most mass manufacturing works today, you might assume that the foundries that make the thinking rocks use nanometer-sized tweezers to place each transistor. If such a tweezer did exist, it wouldn't make any sense to use said tweezer since it would take a long time to place each transistor. (Please refer to the previous section for how big two billion is). Placement by hand isn't feasible, so thinking rocks aren't assembled so much as grown. This happens via a process called photolithography -- also known as lithography. 

Lithography uses light to etch an image onto a silicon wafer (the flattened rock in question). Before the etching occurs, the light passes through a stencil whose design is optically scaled down before the light reaches the chip. Each silicon wafer is coated in a material -- called a photoresist -- which reacts to the light and leaves an etching behind. The newly etched silicon is then chemically treated via a process called doping, which creates the transistors. This process repeats many times, creating a stack of unique layers on the silicone. The completed product is now called the CPU die; it is promptly mounted onto a silicon board that will connect it to the rest of the computer. Lastly, an integrated heat spreader is attached to the top of the CPU die. Its purpose is to efficiently transfer heat away. Without good heat transfer, the CPU would very quickly reach temperatures above 110 C and potentially damage the CPU. 

The entire CPU creation process is executed in a pristine environment called a cleanroom. Given the size of the etchings, a wayward particle would contaminate the process so the rooms must be immaculate. Unfortunately, defects still happen even in a cleanroom. They usually occur because the precision required to perfectly create a CPU is very hard to achieve. Rather than throw the imperfect CPUs away, some foundries engage in a process called binning, which tests the performance of each newly minted CPU. Depending on the defect, the CPU may be able to pass specific benchmarks can be packaged as a cheaper, less powerful, CPU. Once binning is complete, all of the functional CPUs are sent out and eventually make their way into your devices. 

Upon reflection, perhaps a CPU isn't merely thinking rock but a very clever pile of sand, doused in chemicals, and brought to life by lightning. 

 

# Notes:

##### What is a thinking rock exactly 

"switches -- called transistors...": A transistor is an electronically controlled switch that we can turn on or off by applying or removing voltage to the gate. There are two main types of transistors: nMOS devices which allow current when the gate is on, and pMOS devices which allow current when the gate is off. 

"Modern thinking rocks have fancy tricks...": For example, the recursive subtract-and-count method for division is rather slow. There are [faster ways that CPUs do division](https://en.wikipedia.org/wiki/Division_algorithm#Fast_division_methods) such as the Goldschmidt method where $$Q = \frac{N}{D}$$ . The CPU uses binary multiplication to multiply $$N$$ and $$D$$ via a fraction $$F$$ so that $$D$$ approaches 1. As $$D$$ approaches 1, $$N$$ approaches $$Q$$.   

##### A short aside on size and the thinking rock

"Over a billion thinking rocks..." All machines that have a digital component to them [have a thinking rock inside](https://www.scmo.net/logistics-facts) 

"around two billion (or more) transistors..." : High end laptop & desktop CPUs have [around 2 billion transistors](https://en.wikichip.org/wiki/intel/microarchitectures/skylake_(client)#Dual-core). Apple's A13 bionic is reported to have [8.5 billion transistors](https://en.wikichip.org/wiki/apple/ax/a13) and is used in the iPhone 11 series and the iPhone SE2.  Note: do not conflate a higher transistor count with better performance. Mobile devices typically have a System on a Chip (SoC) design which integrates most or all the components of a computer onto the same chip as the CPU. Most of the transistors on an SoC, like the A13 bionic, transistors are used for things other than the CPU. 

"A tower of paper that is 31.07 miles high...": assuming that the thickness of a thin piece of paper is .05 mm, $$5x10^5 m * 1x10^9 = 50,000 m$$. 50,000 m converted to miles is 31.07 miles. 

"That’s halfway to space...': The [Kármán line](https://en.wikipedia.org/wiki/Kármán_line)–which defines the edge of space—is at an altitude of 100 km. 

"Over 4 times as high as the upper ceiling on a commercial airplane...": [“commercial aircraft typically fly between 5.9 to 7.2 miles.”](https://time.com/5309905/how-high-do-planes-fly/#:~:text=Commercial aircraft typically fly between,that can present safety issues.)  The paper stack has a height of 31.07 miles. Thus, $$31.07/7.2 = 4.32$$. 

"5 and half Mt. Everests...": [Mt. Everest is 8,848 meters tall](https://en.wikipedia.org/wiki/Mount_Everest). The paper stack has a height of 50,000 meters. Thus, $$50,000/ 8,848 = 5.65$$.

"112 Empire State Buildings...": To the tip, The Empire State Building is 443.2 meters tall. $$50,000/443.2 = 112.82$$. If we were just judging by roof height it would be over 131 Empire State Buildings stacked on top of each other.

"largest transistor dimension was the length of 400 silicon atoms...": [the transistor gate width is ~80 nm](https://www.intel.com/content/www/us/en/silicon-innovations/intel-14nm-technology.html). The [diameter of silicon atom is .2nm](https://en.wikipedia.org/wiki/Silicon). $$8/.2 = 400$$.  

"cannot be seen by optical microscope...": The wavelength of light at the lower end of the visible light spectrum is ~380 nm. The transistors are smaller than that. Thus, they cannot be seen by human eyes. Instead, one must use more advanced techniques such as a Scanning Electron Microscope.

##### How do we create a thinking rock 

"silicon wafers...": [These wafers are pure silicon.](https://www.intel.com/content/www/us/en/history/museum-making-silicon.html) Silicon has the special property that it doesn't fully conduct or insulate electricity. 

"Lithography uses light...": Because the etched components are very small uniform ultraviolet light is used. The most advanced version of this technique is called [extreme ultraviolet lithography and has a "bandwidth of about 13.5nm."](https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography) It requires lasers and a vacuum chamber.

"stencil's design is scaled down...": The [stencil is called a mask and it contains the circuit pattern](https://computer.howstuffworks.com/euvl1.htm) that is to be etched on the silicon. 

"via a process called doping which creates the transistors...": This process is rather complex [see here for a basic explanation](https://www.halbleiter.org/en/fundamentals/doping/). In short, doping changes the property of the silicon to create the transistors.  

"the CPU may be able to pass certain benchmarks...": For example, Intel historically had 3 different tiers of CPU the i3, i5, and i7. All of those CPUs were created from the same pattern. If a CPU only [passed the benchmarks](https://www.howtogeek.com/403953/how-are-cpus-actually-made) for an i3 (the cheapest and least powerful option) then it would be sold an i3. The next CPU tested may pass all the benchmarks and thus be sold as an i7. These CPUs were from the same batch, but the former suffered some defects that limited its capabilities while the latter did not.



# Further Reading

[Computer Architecture Fundamentals](https://www.techspot.com/article/1821-how-cpus-are-designed-and-built/) 

[CPU Design Process](https://www.techspot.com/article/1830-how-cpus-are-designed-and-built-part-2/)

[Physically Creating a CPU](https://www.techspot.com/article/1840-how-cpus-are-designed-and-built-part-3/)

[Future of CPUs](https://www.techspot.com/article/1853-how-cpus-are-designed-the-future/)

[A comprehensive overview of the 10 nm lithography process](https://en.wikichip.org/wiki/10_nm_lithography_process) 

- Note: the size of the lithography process has long since diverged from the size of the parts being manufactured. 

[More than you want to know about CPU temperatures](https://forums.tomshardware.com/threads/intel-temperature-guide.1488337/) 
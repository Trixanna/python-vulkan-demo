'''
    A simple python implementation of a vulkan api wrapper by realitix
    located here: https://github.com/realitix/vulkan which is a rewrite of
    the original pyvulkin on github. "pip install vulkan"

    I found the triangle demo often cited as overly complicated so this is
    my attempt to write a more simplistic demo while also learning vulkan
    and the API wrapper.
'''
__author__ = "Trixanna"
__date__ = "$Jan 22, 2018 09:50:13 PM$"

import vulkan as vk

application_info = vk.VkApplicationInfo()

instance_create_info = vk.VkInstanceCreateInfo(
    pApplicationInfo=application_info,
    enabledLayerCount=0,
    enabledExtensionCount=0
)

#allocation = vk.vkAllocateMemory()

instance = vk.vkCreateInstance(
    instance_create_info,
    pAllocator=None
)

print("incomplete")

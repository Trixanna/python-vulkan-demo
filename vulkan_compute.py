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

def init_instance():
    ''' Most things set to default values courtesy of the vulkan wrapper to the API '''
    instance_create_info = vk.VkInstanceCreateInfo(
        sType=vk.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
        pApplicationInfo=application_info,
        enabledLayerCount=0,
        enabledExtensionCount=0
    )

    #allocation = vk.vkAllocateMemory()
    instance = vk.vkCreateInstance(
        instance_create_info,
        pAllocator=None
    )

    if vk.VK_SUCCESS == 0:
        print("debug: instance creation success")
    else:
        print("Failed to create instance. Error: {}".format(vk.VK_SUCCESS))

'''
device_info = vk.VkDeviceCreateInfo(
    sType=vk.VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO,
    pNext=None,
    flags=None,
    queueCreateInfoCount=0,
    pQueueCreateInfos=None,
    enabledExtensionCount=0,
    ppEnabledLayerNames=None,
    ppEnabledExtensionNames=None,
    pEnabledFeatures=None,
    enabledLayerCount=0
)'''

def main():
    ''' Temp main runner for development '''
    init_instance()

if __name__ == '__main__':
    main()

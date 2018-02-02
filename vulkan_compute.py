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

def init_instance():
    ''' Most things set to default values courtesy of the vulkan wrapper to the API '''

    application_info = vk.VkApplicationInfo(
        sType=vk.VK_STRUCTURE_TYPE_APPLICATION_INFO
    )

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
    
    return instance

def init_device(instance):
    ''' Enumerate and initialize a device '''
    gpu_count = 0
    gpu_count = vk.vkEnumeratePhysicalDevices(instance,)
    for index, gpus in enumerate(gpu_count):
        print("Enumerated Device: {} _____ {}".format(index, gpus))
    properties = vk.vkGetPhysicalDeviceFormatProperties(
        gpu_count[0],
        vk.VK_FORMAT_B8G8R8_UINT,
    )
    #features = vk.vkGetPhysicalDeviceFeatures(gpu_count[0])

    queue_families = vk.vkGetPhysicalDeviceQueueFamilyProperties(gpu_count[0])
    for index, queue in enumerate(queue_families):
        print("Compute Queue availability for index {} is {}".format(index, bool(queue.queueFlags & vk.VK_QUEUE_COMPUTE_BIT)))

    device_queue_info = vk.VkDeviceQueueCreateInfo(
        sType=vk.VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO,
        queueFamilyIndex=1,
        queueCount=1,
        pQueuePriorities=1.0
    )

    device_info = vk.VkDeviceCreateInfo(
        sType=vk.VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO,
        queueCreateInfoCount=1,
        pQueueCreateInfos=device_queue_info,
        enabledExtensionCount=0,
        ppEnabledLayerNames=None,
        ppEnabledExtensionNames=None,
        pEnabledFeatures=None,
        enabledLayerCount=0
    )
    device = vk.vkCreateDevice(
        gpu_count[0],
        pCreateInfo = None,
        pAllocator = 0
    )

    return device


def destroy_device(device):
    vk.vkDestroyDevice(device, pAllocator=0,)

def main():
    ''' Temp main runner for development '''
    instance = init_instance()
    device = init_device(instance)

    index = [1, 2, 3, 4, 5]
    queue = vk.vkGetDeviceQueue(device, 1, index)

    destroy_device(device)
    vk.vkDestroyInstance(instance, 0)

if __name__ == '__main__':
    main()
    # Notes: This isn't exactly what I was going for, but the cdata and structures mean that I have to re-think
    # My plans for this vulkan_compute model. I will pick it up again later.

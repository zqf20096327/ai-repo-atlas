# BoumedineBillal/esp32-p4-jit

⭐ 57 · Assembly · MIT · 推送 2026-01-01 · [GitHub](https://github.com/BoumedineBillal/esp32-p4-jit) · 个人维护

**ESP32-P4 动态代码加载系统：PC 编译、设备原生执行，免刷固件**

面向嵌入式开发者的动态 RISC-V 编译与执行系统：在 PC 端编译 C/C++ 代码，经 USB 加载到 ESP32-P4 上以原生机器码执行，部署周期 1-2 秒，无需重刷固件。提供 Python/NumPy 接口，支持自动类型转换与内存管理、多文件 LTO 编译、调用固件符号（printf/malloc/FreeRTOS）、类型与内存安全校验。需先安装 ESP-IDF v5.x 工具链并配置路径，再刷入配套固件方可使用。附 Jupyter 教程与示例，含 INT8 MNIST CNN 在 PIE SIMD 指令上的部署演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PC 端编译、ESP32-P4 原生执行，1-2 秒部署周期
- NumPy ↔ C 自动类型转换与双向数组同步
- 多文件自动发现与 LTO 链接，符号桥接调用固件函数
- 支持在真实硬件上测试 ESP32-P4 PIE SIMD 指令（模拟器不可测）

## 适用场景

- DSP 算法与音频处理的快速原型迭代
- 在真实硅片上调试硬件专属 SIMD 指令内核
- 嵌入式 ML 内核（如 INT8 CNN）的部署与性能测量
- 免刷固件反复试验 C 代码逻辑

## 场景标签

 · 领域:嵌入式系统/开发工具

## 证据(README 行号)

> L5:  Compile C/C++ on your PC, execute natively on ESP32-P4 — No firmware reflashing required.
> L9: P4-JIT is a sophisticated dynamic code loading system that enables you to write, compile, and execute native RISC-V 
> L31: ### 📗 Tutorial 2: MNIST Classification

## 星数曲线

```mermaid
xychart-beta
    title "BoumedineBillal/esp32-p4-jit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 55 --> 58
    line [56, 57, 57]
```

2026-10-18 56 → 2026-10-29 57（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `e33b8604bee7` · [字段定义](../../DATASET.md)*

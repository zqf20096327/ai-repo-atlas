# kerlenton/bootgpt

⭐ 50 · Python · MIT · 推送 2026-10-31 · [GitHub](https://github.com/kerlenton/bootgpt) · 个人维护

**在 512 字节 MBR 引导扇区里运行的语言模型：开机即生成假 Linux 启动日志**

由手写 16 位实模式汇编构成的 MBR（512 字节）加载随后 23 个扇区中的 11.5KB int8 模型，在 386 上无 OS、无 C 运行时地执行前向推理，逐字符生成伪造的 Linux dmesg 启动日志（时间戳、PCI、ACPI 条目）。模型为字符嵌入+单隐层+softmax，用 Python 训练并量化为 int8（2 的幂尺度），训练脚本模拟汇编的整数运算与 LCG 采样，Python 输出与引导扇区输出逐字符一致。产物 disk.img 可 dd 到 USB 在 BIOS 机器上启动，或用 QEMU 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完整推理引擎装进 510 字节 MBR，权重与词表放在数据扇区
- int8 量化（2 的幂尺度），前向传播仅用 imul 与一次 idiv
- Python 侧模拟精确整数运算与 LCG 采样，与引导扇区输出逐字符一致
- corpus_gen.py 生成 3MB 伪 dmesg 语料，每次会话固定内核版本与磁盘

## 适用场景

- 用 QEMU 或 BIOS 机器直接启动观看模型生成启动日志
- 学习 sizecoding 与无 OS 神经网络推理的实现
- 研究极小字符级模型的量化与整数算术仿真

## 场景标签

 · 领域:创客/演示场景（demoscene）× 神经网络

## 证据(README 行号)

> L3: A neural network that boots your PC.
> L5: The MBR is 512 bytes of hand written asm. It loads an 11.5 KB int8 model
> L6: from the next 23 sectors and runs it in 16-bit real mode on a 386. No OS,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 mid · 依据 README sha `4f0762f45808` · [字段定义](../../DATASET.md)*

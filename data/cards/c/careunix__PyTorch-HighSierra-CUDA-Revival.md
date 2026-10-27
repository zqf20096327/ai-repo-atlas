# careunix/PyTorch-HighSierra-CUDA-Revival

⭐ 27 · Python · 推送 2025-11-14 · [GitHub](https://github.com/careunix/PyTorch-HighSierra-CUDA-Revival) · 个人维护

**为 macOS High Sierra 复活 CUDA 深度学习栈的 PyTorch 定制构建**

提供在 macOS 10.13.6 上运行的 PyTorch 1.7.0a0 自定义 CUDA 构建的 wheel 包（cp38），搭配 NVIDIA CUDA 10.2、cuDNN 7.6.5 与 NVIDIA WebDriver，使 Pascal 架构 GTX 显卡可在该系统上执行 GPU 加速的深度学习计算。面向仍持有旧 Mac + NVIDIA 显卡的研究者与开发者；仓库同时承担数字保存职能，收录构建日志、NVCC 标志、wheel 哈希与可复现环境清单，并提供兼容性矩阵、故障排查与源码重建文档。无 CUDA 时 wheel 可退回 CPU 后端正常使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 1.7.0a0 自定义 CUDA 构建 wheel（macOS 10.13.6 / Python 3.8）
- 覆盖 Pascal 全系（GTX 1050–1080 Ti / Titan Xp）及 Kepler 等 WebDriver 兼容显卡
- 提供 SHA256 校验与 GPG 签名验证流程
- 归档构建日志、环境清单与重建文档，支持可复现构建

## 适用场景

- 在 High Sierra + Pascal 显卡的旧 Mac 上继续 GPU 训练/推理（如 GPT-2 示例）
- 复现并重建 macOS 最后一个 CUDA 深度学习环境
- 查阅 macOS CUDA 停更时间线与兼容性资料

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L29: This project restores full CUDA compute support on macOS High Sierra using NVIDIA CUDA 10.2, cuDNN 7.6.5, and a cus
> L73: |PyTorch|**1.7.0a0 (Custom CUDA Build)**|✔ Working|

## 星数曲线

```mermaid
xychart-beta
    title "careunix/PyTorch-HighSierra-CUDA-Revival 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `97cd09133f75` · [字段定义](../../DATASET.md)*

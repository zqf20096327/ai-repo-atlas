# Neutone/neutone_sdk

⭐ 633 · Python · LGPL-2.1 · 推送 2025-12-05 · [GitHub](https://github.com/Neutone/neutone_sdk) · 组织维护

**将 PyTorch 神经音频模型封装为 VST 插件可加载格式的 SDK**

面向 AI 音频研究者的开源框架：用少量 Python 代码封装 PyTorch 音频模型，导出为 .nm 文件，由免费的宿主插件 Neutone FX（实时）与 Neutone Gen（非实时，beta）加载进 DAW 运行。SDK 在统一接口内处理可变缓冲区大小、采样率转换、延迟补偿与控制参数（四个旋钮），并提供基准测试与性能分析 CLI 工具。导出时自动运行检查确保模型可被插件加载。研究者也可将模型贡献到插件内置模型库；已被用于音色迁移、音频效果仿真、样本生成等场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Python 封装 PyTorch 模型导出 .nm 文件，无需 C++ 知识
- 自动处理缓冲区、采样率/声道转换与延迟补偿
- 基准测试与 CPU/内存性能分析 CLI 工具
- 配套 VST3/AU 宿主插件 Neutone FX 与 Neutone Gen

## 适用场景

- 把训练好的神经音频模型带入 DAW 做实时/离线效果处理
- 研究者在不写 C++ 插件代码的情况下发布音频模型
- 对封装模型在多种 DAW 参数组合下做延迟与速度基准测试

## 场景标签

 · 领域:音频/音乐技术

## 证据(README 行号)

> L10: The Neutone SDK is an open source framework that streamlines the deployment of PyTorch-based neural audio models fo
> L11: It enables researchers to wrap their own PyTorch audio models and run them in the DAW using our free host plugins N
> L13: By encapsulating common challenges such as variable buffer sizes, sample rate conversion, delay compensation, and c

## 星数曲线

```mermaid
xychart-beta
    title "Neutone/neutone_sdk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 632 --> 635
    line [634, 633, 633]
```

2026-10-18 634 → 2026-10-29 633（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `7b57065f8808` · [字段定义](../../DATASET.md)*

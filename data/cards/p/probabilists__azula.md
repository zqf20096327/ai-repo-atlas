# probabilists/azula

⭐ 134 · Python · MIT · 推送 2026-08-28 · [GitHub](https://github.com/probabilists/azula) · [官网](https://azula.readthedocs.io) · 组织维护

**PyTorch 扩散模型库：统一文献形式体系的生成式建模接口**

实现扩散模型的 Python 库，将扩散模型文献中不同的形式体系与记号统一到单一接口：扩散模型由噪声调度、去噪器与采样器三要素组合构成，API 直接对应该形式体系。提供从源码安装最新功能的方式，并通过插件接口加载预训练模型（如 adm 插件）以同样接口使用，配套 readthedocs 文档与教程。以 pip 包形式提供给使用 PyTorch 做生成式建模研究的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将扩散模型统一为噪声调度 + 去噪器 + 采样器三要素的组合形式体系
- 内置 KarrasDenoiser、VPSchedule、DDPM/DDIM 采样器等组件
- 插件接口支持加载预训练模型并用统一接口采样
- 配套 readthedocs 文档与教程

## 适用场景

- 用统一接口快速搭建与实验不同的扩散模型组合
- 加载预训练扩散模型进行 DDIM 等方式采样
- 学习扩散模型文献中不同形式体系的对应实现

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: Azula is a Python package that implements diffusion models in PyTorch. Its goal is to unify the different formalisms
> L25: In Azula's formalism, a diffusion model is the composition of three elements: a noise schedule, a denoiser and a sa

## 星数曲线

```mermaid
xychart-beta
    title "probabilists/azula 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 133 --> 135
    line [134, 134]
```

2026-10-18 134 → 2026-10-27 134（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2584d00aa656` · [字段定义](../../DATASET.md)*

# lucidrains/autoregressive-diffusion-pytorch

⭐ 441 · Python · MIT · 推送 2026-09-02 · [GitHub](https://github.com/lucidrains/autoregressive-diffusion-pytorch) · 个人维护

**PyTorch 实现的无向量量化自回归图像生成架构库**

论文 Autoregressive Image Generation without Vector Quantization 架构的 PyTorch 复现，供研究者在图像生成任务中使用。提供 AutoregressiveDiffusion 与面向图像 token 序列的 ImageAutoregressiveDiffusion 模型类，附带图像训练器；另提供基于 flow matching 的变体（ImageAutoregressiveFlow / AutoregressiveFlow），接口用法与主类一致。以 pip 包形式安装，README 展示示例生成结果（oxford flowers 96k 步）并列出多篇引用文献。

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

- 提供 AutoregressiveDiffusion 与图像 token 序列变体两类模型类
- 附带图像训练器（Trainer）
- 提供基于 flow matching 的替代实现（AutoregressiveFlow 系列）

## 适用场景

- 研究无向量量化的自回归生成架构
- 复现或扩展论文中的图像生成实验
- 对比扩散与 flow matching 两种训练路径

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: Implementation of the architecture behind Autoregressive Image Generation without Vector Quantization in Pytorch
> L48: For an improvised version using flow matching, just import `ImageAutoregressiveFlow` and `AutoregressiveFlow` inste

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/autoregressive-diffusion-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 440 --> 442
    line [441, 441]
```

2026-10-18 441 → 2026-10-30 441（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f3389608c550` · [字段定义](../../DATASET.md)*

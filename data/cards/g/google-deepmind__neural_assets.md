# google-deepmind/neural_assets

⭐ 21 · Python · Apache-2.0 · 推送 2026-05-08 · [GitHub](https://github.com/google-deepmind/neural_assets) · 组织维护

**3D 感知多物体场景图像合成的 JAX 研究代码**

Neural Assets 论文的官方代码实现：用 JAX 编写，包含从输入数据提取物体外观与位姿 token 的条件编码器，以及以这些 token 为条件的扩散图像生成器。附带示例 notebook，演示从公开数据集 MOVi 加载处理视频数据、构建模型并计算训练损失。限制：不含完整训练循环，模型内部封装 Stable Diffusion；Python 3.13 及以上版本不支持。安装通过 venv 与 requirements.txt，另需克隆 big_vision 的 ViT 实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JAX 实现：条件编码器提取外观与位姿 token，扩散生成器条件合成
- 示例 notebook 演示 MOVi 数据集加载与训练损失计算
- 代码不含完整训练循环
- 不支持 Python 3.13 及以上版本

## 适用场景

- 复现论文方法并计算训练损失
- 在 MOVi 数据集上运行 3D 感知场景合成模型
- 基于 token 条件扩散生成机制做后续研究

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L11: The code here provides an implementation of our Neural Assets framework in jax,
> L12: including a conditioning encoder to extract the appearance and pose tokens from
> L13: input data, and a diffusion-based image generator conditioned on the tokens.

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/neural_assets 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fb423057bb30` · [字段定义](../../DATASET.md)*

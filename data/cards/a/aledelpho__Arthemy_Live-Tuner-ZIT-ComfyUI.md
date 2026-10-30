# aledelpho/Arthemy_Live-Tuner-ZIT-ComfyUI

⭐ 15 · Python · Apache-2.0 · 推送 2026-01-28 · [GitHub](https://github.com/aledelpho/Arthemy_Live-Tuner-ZIT-ComfyUI) · 个人维护

**ComfyUI 节点集：免训练实时调整 Z-Image 与 Qwen 编码器权重分片**

面向 ComfyUI 用户的自定义节点集：将 Z-Image 的 S3-DiT 30 层与 Qwen3-4B 文本编码器 36 层划分为功能区块（6 位置块 / 6 语义区），用滑块对各区权重做实时缩放，无需训练即可影响构图、光照、细节或提示词遵循度；另提供逐层控制的 LAB 版本与序列化保存节点。Z-Image 调参需配套专用 Loader 以避免缓存导致的权重累积。作者声明功能块边界为实验性，项目处于 Work in Progress。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 将 Z-Image 模型 30 层切分为 6 位置块并用滑块缩放权重
- Qwen3-4B 文本编码器 36 层分为 6 语义区独立调节
- LAB 版本暴露全部 66 个层供逐层实验
- Saver 节点可将调参后权重序列化为 .safetensors 文件

## 适用场景

- 不改训练就调整 Z-Image 出图的构图与细节倾向
- 调节 Qwen 文本编码器各层观察提示词解读变化
- 逐层实验寻找控制特定视觉属性的层并保存权重

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Advanced real-time control for **Z-Image** models and **Qwen3-4B** Text Encoders. These nodes perform "live surgery"
> L14: I developed these nodes to slice the monolithic **S3-DiT** of **Z-Image** to give you more control over different s
> L118: 2. Run: `git clone https://github.com/aledelpho/ComfyUI-Arthemy-ZImage-Tuner.git`

## 星数曲线

```mermaid
xychart-beta
    title "aledelpho/Arthemy_Live-Tuner-ZIT-ComfyUI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `662718408c2b` · [字段定义](../../DATASET.md)*

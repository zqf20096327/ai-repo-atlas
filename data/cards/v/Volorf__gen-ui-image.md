# Volorf/gen-ui-image

⭐ 20 · C# · MIT · 推送 2026-01-01 · [GitHub](https://github.com/Volorf/gen-ui-image) · [官网](https://volorf.github.io/) · 个人维护

**Unity 包：用 AI 生成 UI 图片辅助快速原型**

面向 Unity 开发者的 UI 图片生成包：在编辑器中创建 Gen UI Image 组件，输入 prompt 调用 OpenAI 图像模型（dall-e-2/dall-e-3/gpt-image-1）生成占位图或界面图，可保存为 Asset 或在运行时通过 Generate() 生成并读取 Texture2D。API Key 经 PlayerPrefs 本地存储，也可在运行时显式传入；打包场景需附加 ApiKeysProvider 组件。要求 Unity 2022.3 或更高版本，通过 Package Manager 从 Git URL 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 dall-e-2 / dall-e-3 / gpt-image-1 三个 OpenAI 模型
- 生成图片可保存为 Asset 或直接获取 Texture2D
- 运行时可通过 C# 调用 Generate() 并指定模型/尺寸/质量
- API Key 支持 PlayerPrefs 存储或运行时显式传入

## 适用场景

- Unity 原型阶段快速生成 UI 占位图
- 为产品卡片等界面生成预览图片
- 运行时按 prompt 动态生成贴图

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L2: Create a UI image with AI-generated content in Unity.
> L17: Right now, `Gen UI Image` supports only **OpenAI** API.
> L20: * `dall-e-2`

## 星数曲线

```mermaid
xychart-beta
    title "Volorf/gen-ui-image 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `cffd9c4cd38a` · [字段定义](../../DATASET.md)*

# ru4ls/ComfyUI_Nano_Banana

⭐ 61 · Python · MIT · 推送 2026-03-02 · [GitHub](https://github.com/ru4ls/ComfyUI_Nano_Banana) · 个人维护

**ComfyUI 自定义节点集：通过 Gemini API/VertexAI 做文生图与图编辑**

面向 ComfyUI 用户的自定义节点集，调用 Google Generative AI SDK 与 Vertex AI 两种通道，使用 Gemini 图像模型（gemini-3-pro-image-preview、gemini-3.1-flash-image-preview）进行文生图、图生图、多图融合与多轮对话式编辑。AIO 节点支持最多 10 张输出、6 张参考图（Nano Banana 2 节点支持 14 张参考图）、多种宽高比与 1K/2K/4K 分辨率、Google 搜索与图像搜索接地，并输出思考过程（仅 Vertex AI）与接地来源。需要 Google API key 或 Google Cloud 项目，Gemini API 为付费服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AIO 节点支持文生图/图生图/多图融合与 1-10 张批量生成
- 多轮对话节点保留上下文做迭代式图像编辑
- Nano Banana 2 节点支持 14 张参考图、极端宽高比与 Google 图像搜索接地
- 双通道认证：Gemini API key 或 Vertex AI（ADC），自动检测可用凭证

## 适用场景

- 在 ComfyUI 工作流中用 Gemini 图像模型生成或编辑图片
- 通过多轮对话节点迭代式修图
- 用 Vertex AI 通道获取思考过程与接地来源

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L7: A set of custom nodes for ComfyUI that leverage both Google Vertex AI and Google Generative AI SDK to generate image
> L82: You can use either Google Generative AI API approach (simpler) or Google Vertex AI approach (more powerful) dependi

## 星数曲线

```mermaid
xychart-beta
    title "ru4ls/ComfyUI_Nano_Banana 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-26 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `8d27358416df` · [字段定义](../../DATASET.md)*

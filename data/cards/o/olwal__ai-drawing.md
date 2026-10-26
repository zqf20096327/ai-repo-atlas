# olwal/ai-drawing

⭐ 35 · C++ · MIT · 推送 2025-12-20 · [GitHub](https://github.com/olwal/ai-drawing) · 个人维护

**C++ 实时人机协作绘画应用：AI 视觉解读加扩散补全**

基于 Cinder 框架的交互式 C++ 绘画应用：用户无需输入提示词，直接在画布上绘画；Ollama 视觉模型（默认 llava:7b）通过 OllamaClientCinder 客户端实时分析画面生成语义描述，StreamDiffusionSpoutService 接收画面与描述执行实时 image-to-image 扩散，生成结果经 Spout GPU 纹理共享回传并与原画合成。绘图、推理、生成分线程运行。构建依赖 Visual Studio 2022、Cinder 框架、Ollama 与独立的 StreamDiffusionSpoutService 服务，扩散服务端仅支持 Windows（Spout）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无提示词绘画：VLM 实时解读 + StreamDiffusion 实时图生图补全
- 自带 OllamaClientCinder C++ 客户端，支持 Cinder/OpenFrameworks、异步与视觉模型
- Spout 零拷贝 GPU 纹理共享与 OSC 消息（TouchDesigner/Max/MSP 通信）
- 绘图、推理、生成多线程并发，ThreadSafeList 同步

## 适用场景

- 在画布上随手画，让 AI 实时补全和增强画面
- 与 TouchDesigner 等 creative coding 工具联动做实时视觉表演
- 研究无需文本提示的闭环 AI 协作创作流程

## 场景标签

`图像生成` `多模态` · 领域:内容生成

## 证据(README 行号)

> L5: An interactive C++ drawing application that combines AI-powered visual completion through real-time canvas interpret
> L11: - **AI Canvas Analysis**: Real-time interpretation of drawings using Ollama vision models
> L12: - **AI Image Generation**: Real-time augmentation of drawings through diffusion models

## 星数曲线

```mermaid
xychart-beta
    title "olwal/ai-drawing 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-26 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `97151a2374da` · [字段定义](../../DATASET.md)*

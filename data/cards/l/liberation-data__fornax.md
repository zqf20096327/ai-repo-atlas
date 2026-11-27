# liberation-data/fornax

⭐ 3 · Java · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/liberation-data/fornax) · [官网](https://fornax4j.org/) · 组织维护

**让 Java 开发者在 JVM 内以方法调用方式运行本地开源生成模型**

通过 Java FFM API 直接绑定 llama.cpp、stable-diffusion.cpp、acestep.cpp、yue2.cpp、whisper.cpp、stems.cpp 等原生推理引擎，在 JVM 内以普通 Java 方法调用语言、视觉、语音、图像、歌曲等开放权重模型，无 Python、无模型服务器、无 HTTP 往返。按 Maven Central 发布模块（fornax-llama/sd/tts/whisper 等）与平台 natives jar，经 Vulkan/Metal 后端运行在 GPU 上，无 GPU 时默认停止运行。提供 ModelPool、worker 进程隔离、Dispatch 多模型调度与 Fornax Studio 图形界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- FFM API 直接绑定 llama.cpp/stable-diffusion.cpp 等 C/C++ 引擎，无 Python 与模型服务器中间层
- 模块覆盖文本生成、图像生成/编辑、TTS、歌曲生成、语音识别、音轨分离
- 支持 OpenAI 格式的 tool calling、JSON schema 约束输出、嵌入与重排序模式
- ModelPool 按 LRU 卸载模型，Dispatch 以 worker 进程调度多模型与 QoS 队列

## 适用场景

- 在 Java 应用内直接调用 GGUF 语言模型做对话与工具调用
- 用视觉语言模型把发票等图像转成 schema 校验的 JSON
- 在 JVM 内做图像生成、语音转文字或歌曲合成
- 服务端按内存预算常驻与调度多个本地模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: **Call open-weight models (language, vision, speech, images, songs, video) as plain Java methods, running on your GP
> L21: - **The native runners themselves.** Fornax calls llama.cpp, stable-diffusion.cpp, acestep.cpp, yue2.cpp,
> L29: Fornax binds native inference engines with Java's Foreign Function & Memory API (Java 22+; Kiln 0.1.0 itself needs 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `e1345106d987` · [字段定义](../../DATASET.md)*

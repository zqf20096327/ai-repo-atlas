# ngxson/wllama

⭐ 1,408 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/ngxson/wllama) · [官网](https://huggingface.co/spaces/ngxson/wllama) · 个人维护

**在浏览器内直接运行 llama.cpp 进行 LLM 推理的 Wasm 绑定库**

将 llama.cpp 编译为 WebAssembly 的 JavaScript 绑定，使 LLM 推理直接在浏览器内运行，无需后端或 GPU。提供全类型内置的 OpenAI 兼容 API、WebGPU 加速（GPU 显存不足时部分层回退 CPU）、多模态输入（图像/音频/视频）、语音功能（TTS、转录、实时全双工会话）与工具调用。模型以 GGUF 文件直接加载，缓存于 OPFS，支持大于 4GB 的文件自动分片。限制：多线程需配置 COEP/COOP 响应头，跨 worker 分片需 JSPI 或 compat 构建。npm 包自带预编译二进制；从源码构建需 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器内直接推理（WebAssembly SIMD），无需后端或 GPU
- WebGPU 支持，显存不足时自动 CPU 回退与 n_gpu_layers 分层配置
- OpenAI 兼容 API、工具调用与多模态（图像/音频/视频）输入
- 语音：TTS、转录、实时 ASR 与全双工会话，事件模型对齐 OpenAI Realtime API

## 适用场景

- 在纯前端网页应用中离线运行 GGUF 模型做对话与补全
- 浏览器内生成文本嵌入并计算余弦相似度
- 网页端实现语音聊天、实时转写或语音翻译
- 部署视觉多模态补全的 Web demo

## 场景标签

`推理引擎` `语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L3: WebAssembly binding for llama.cpp
> L26: - Can run inference directly on browser (using WebAssembly SIMD), no backend or GPU is needed!

## 星数曲线

```mermaid
xychart-beta
    title "ngxson/wllama 星数(近 21 点)"
    x-axis ["2026-10-21", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-30", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 1336 --> 1412
    line [1342, 1349, 1350, 1351, 1352, 1353, 1355, 1351, 1364, 1385, 1386, 1387, 1390, 1391, 1393, 1395, 1397, 1399, 1402, 1406, 1406]
```

2026-10-21 1,342 → 2026-11-24 1,406（+64）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `7304562660b5` · [字段定义](../../DATASET.md)*

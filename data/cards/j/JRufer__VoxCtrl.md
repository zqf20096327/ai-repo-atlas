# JRufer/VoxCtrl

⭐ 29 · Rust · MIT · 推送 2026-10-27 · [GitHub](https://github.com/JRufer/VoxCtrl) · [官网](https://jrufer.com/voxctrl/) · 个人维护

**本地离线语音转文字听写应用，可将语音路由到任意应用或服务**

用 Rust/Tauri 2/Svelte 5 构建的桌面语音输入代理：支持 whisper.cpp（GGUF/Vulkan/CUDA）、Moonshine ONNX、Parakeet TDT 等多引擎离线语音识别，可选用 OpenAI 兼容远程转写端点；内置 llama.cpp 运行 S1-mini 模型做文本规范化。转写结果可路由到 11 种目标（注入窗口、剪贴板、shell、socket、文件、webhook、对话 LLM 等），支持语音命令、6 种离线 TTS 引擎、HUD 悬浮显示、MCP 服务器。提供 Linux AppImage/.deb 与 Windows 安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- whisper.cpp / Moonshine / Parakeet TDT 多引擎离线 STT，支持 Vulkan/CUDA/WebGPU 加速与 CPU 回退
- 11 种输出路由目标（inject/clipboard/exec/socket/webhook/chat 等）与语音命令分发
- 6 种离线 TTS 引擎（含语音克隆）与空闲内存自动卸载
- 内置 MCP 服务器，向 Claude Desktop、Cursor 等客户端暴露 transcribe/speak 工具

## 适用场景

- 离线语音听写，直接输入到任意编辑器或终端
- 把语音分发到脚本、webhook、智能家居等自定义目标
- 作为语音工具接入本地 LLM 对话助手

## 场景标签

`语音识别` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L5: A high-performance, private, on-device voice-to-text dictation application and programmable **voice input broker** b
> L9: VoxCtrl acts as an intelligent desktop voice gateway, routing speech to any destination—typing directly into focused

## 星数曲线

```mermaid
xychart-beta
    title "JRufer/VoxCtrl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-30 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `1b9207abd301` · [字段定义](../../DATASET.md)*

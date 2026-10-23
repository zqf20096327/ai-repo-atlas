# vakovalskii/NeuralDeskApp

⭐ 331 · TypeScript · NOASSERTION · 推送 2026-05-15 · [GitHub](https://github.com/vakovalskii/NeuralDeskApp) · [官网](https://t.me/neuraldeep) · 个人维护

**跨平台桌面 AI 助手，支持本地模型与工具调用**

基于 React + Tauri + TypeScript 的桌面 AI 助手，面向开发者、研究者和 AI 爱好者。通过 OpenAI SDK 兼容任意 OpenAI 格式端点，支持 vLLM、Ollama、LM Studio 本地推理。功能包括：任务规划与定时任务、JS/Python 代码沙箱执行、PDF/DOCX 文档提取（内置、开箱即用）、Tavily/Z.AI 网络搜索、Telegram 频道渲染、持久记忆（~/.valera/memory.md）、SQLite 会话存储、每轮完整请求/响应日志。文件操作限制在工作区目录内。语音输入需额外启动本地转录服务器。构建需 Rust 1.74+、Node.js 20+；Windows/macOS/Linux 可打包安装。限制：License 要求年收入超 100 万美元的组织购买商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI SDK 兼容任意 OpenAI 格式端点，支持 vLLM/Ollama/LM Studio 本地模型
- 20+ 个工具：文件操作、代码沙箱、网络搜索、定时任务、记忆管理
- 每轮完整请求/响应 JSON 日志与 token/时长追踪
- Tauri 打包，支持 Windows 安装包、macOS DMG、Linux AppImage

## 适用场景

- 在本地用 Ollama/vLLM 运行模型并保持对话私密
- 调试和对比 Qwen、Llama、DeepSeek 等模型的 API 调用
- 通过定时任务与工具调用自动执行提醒和脚本

## 场景标签

 · 领域:桌面 AI 应用

## 证据(README 行号)

> L9: **Desktop AI Assistant with Local Model Support**
> L18: - ✅ **OpenAI SDK** — full API control, compatible with any OpenAI-compatible endpoint
> L19: - ✅ **Local Models** — vLLM, Ollama, LM Studio support

## 星数曲线

```mermaid
xychart-beta
    title "vakovalskii/NeuralDeskApp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 330 --> 332
    line [331, 331]
```

2026-10-18 331 → 2026-10-23 331（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e7c27323c922` · [字段定义](../../DATASET.md)*

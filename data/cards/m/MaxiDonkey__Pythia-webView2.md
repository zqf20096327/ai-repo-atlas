# MaxiDonkey/Pythia-webView2

⭐ 14 · JavaScript · MIT · 推送 2026-06-10 · [GitHub](https://github.com/MaxiDonkey/Pythia-webView2) · 个人维护

**给 Delphi 桌面应用嵌入 AI 聊天工作区的 VCL/FMX 组件**

基于 Microsoft WebView2 的 Delphi VCL/FMX 组件，在桌面应用中嵌入 ChatGPT/Claude 式聊天界面：聊天窗口、流式显示、模型选择器、附件、函数/MCP/skills/agents 卡片、斜杠命令、会话、主题与 23 种语言国际化。它只标准化交互层，不做厂商调用——应用收到结构化提示状态后自行通过 OpenAI/Anthropic/Gemini/Mistral 等 SDK 发起请求。仓库含 8 个可运行示例（含 Anthropic 与 OpenAI 接入演示）与插件示例，要求 Delphi 11/12/13、Windows、WebView2 Runtime，依赖 WebView4Delphi。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- VCL/FMX 组件提供聊天界面、流式显示、会话、卡片、斜杠命令等交互层
- 厂商调用保留在 Delphi 侧，不做统一 LLM 抽象
- 知识文件索引进向量存储用于 RAG（上传→嵌入→就绪）
- 内置麦克风采集与厂商语音转文字输入
- 仓库含 8 个可运行示例，覆盖 starter/vendor/plugin 三类

## 适用场景

- 给 Delphi 桌面应用加一个 AI 聊天工作区界面
- 保持厂商调用与业务逻辑在 Delphi 代码内可控
- 通过插件扩展自定义斜杠命令与宿主侧逻辑

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L195: |Vendor integration|Defined by the host|**Pythia-Webview2** exposes the state; the application chooses how to call

## 星数曲线

```mermaid
xychart-beta
    title "MaxiDonkey/Pythia-webView2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `dd52d1a162a1` · [字段定义](../../DATASET.md)*

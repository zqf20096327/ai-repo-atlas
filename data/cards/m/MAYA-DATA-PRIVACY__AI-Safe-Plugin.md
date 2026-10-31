# MAYA-DATA-PRIVACY/AI-Safe-Plugin

⭐ 35 · JavaScript · MIT · 推送 2026-10-03 · [GitHub](https://github.com/MAYA-DATA-PRIVACY/AI-Safe-Plugin) · 组织维护

**浏览器插件：在 AI 聊天界面实时检测并遮蔽个人敏感信息**

Chrome 扩展加本地服务器组合，在用户向 AI 聊天网站提交文本前拦截检测 PII：本地运行 GLiNER2 ONNX 模型识别人名、邮箱、电话、信用卡、SSN 等实体，辅以内置与自定义正则规则（API key、JWT、私钥等），以内联高亮方式提示用户一键遮蔽。适用于 ChatGPT、Claude、Gemini、Perplexity 等任意含文本输入的网站。可选开启 Maya 匿名化服务以生成拟真替代值（默认关闭，需 Maya API key）。本地服务器通过一键脚本安装（curl/PowerShell），绑定 127.0.0.1:8765，支持 Linux/macOS/Windows 自启动。限制：不防护已提交后服务端处理，也不防护恶意扩展或键盘记录器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 GLiNER2 ONNX 模型检测，离线可用，无需云端调用
- 正则规则覆盖 API key/JWT/SSN 等，支持自定义模式
- Grammarly 式内联高亮，一键遮蔽或忽略，含键盘快捷键
- 一键脚本安装本地服务器并注册自启动（Linux/macOS/Windows）

## 适用场景

- 在 ChatGPT/Claude/Gemini 等聊天框中发送前遮蔽姓名、邮箱、证件号等敏感信息
- 防止误粘贴 API key、JWT、私钥等凭据到网页输入框
- 按工作流自定义内部 ID 的检测规则

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L24: MAYA AISafe Plugin sits between you and the AI. It watches what you type, spots sensitive information in real time,
> L38: - **Local detection by default** - GLiNER2 ONNX model runs on localhost. Detection does not require cloud calls and

## 星数曲线

```mermaid
xychart-beta
    title "MAYA-DATA-PRIVACY/AI-Safe-Plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `24f2c16653b5` · [字段定义](../../DATASET.md)*

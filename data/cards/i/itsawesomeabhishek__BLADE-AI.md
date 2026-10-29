# itsawesomeabhishek/BLADE-AI

⭐ 18 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/itsawesomeabhishek/BLADE-AI) · 个人维护

**用自然语言指令卸载安卓预装应用的桌面工具**

基于 Electron + React + Python 的 Android 精简（debloat）桌面应用，通过 ADB 连接设备。用户在聊天界面输入如 remove all xiaomi bloatware 的指令，OpenClaw 引擎解析意图并识别包名，Perplexity AI（Sonar 模型）提供安全评级与风险分析，破坏性操作需明确确认；Action Mode 可切换为仅顾问模式。支持扫描、批量卸载、备份与恢复。需 ADB、USB 调试与 Perplexity API Key，提供 Windows/Linux/macOS 安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言指令驱动 ADB 卸载，意图解析由 OpenClaw 完成
- Perplexity AI 提供每个包的安全评级与风险分析
- Action Mode 开关：执行模式或仅顾问分析模式
- 完整备份与一键恢复，破坏性操作需多重确认

## 适用场景

- 用自然语言批量卸载手机预装/臃肿应用
- 扫描设备并查看各包的卸载风险分析
- 清理前做全量备份，出错后一键恢复

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L14:  The first AI-powered Android debloater. Remove bloatware using natural language commands.
> L51: Toggle **Action Mode** ON to let the chatbot execute commands directly. Toggle it OFF to use the chatbot as an advi
> L60: - **AI Chat Interface** — Natural language interaction powered by Perplexity AI

## 星数曲线

```mermaid
xychart-beta
    title "itsawesomeabhishek/BLADE-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `bcdd714781aa` · [字段定义](../../DATASET.md)*

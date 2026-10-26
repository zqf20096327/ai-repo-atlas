# VyomKulshrestha/Heliox-OS

⭐ 68 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/VyomKulshrestha/Heliox-OS) · [官网](https://www.helioxos.dev) · 个人维护

**本地优先的桌面 AI 代理：用语音/文本/手势/眼动控制并自动化电脑操作**

MIT 许可的跨平台（Windows/macOS/Linux）桌面 agent 应用：把打字或语音请求转为经验证的计划，经五级权限门与风险审批后路由给专家执行器本地执行，并对结果做验证与可撤销处理。支持连续语音（Faster-Whisper/Whisper）、30+ 手势映射、粗粒度眼动融合、浏览器/文件/进程/Git 等操作、持久后台任务、MCP 接口、插件市场与神经意图（EEG）研究。默认本地运行守护进程与支持的本地模型，但涉及云模型或第三方集成的任务会向其发送所需上下文。发布版本 v0.14.0，Python 3.11+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 162 个声明动作类型，21 个可执行专家，五级权限门与逐动作审批
- 连续语音识别（Faster-Whisper/Whisper）、30+ 手势映射与眼动融合
- 文件/剪贴板等操作的每任务 Undo 与 Ed25519 签名回执
- 公开的能力目录、基准数据与限制边界说明

## 适用场景

- 用自然语言或语音让代理代为操作浏览器、文件与系统
- 免手操作：语音、手势与眼动等替代输入路径控制电脑
- 需要审批与审计的自动化后台工作流

## 场景标签

`GUI 自动化` `AI 助手` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12:  Control your computer with natural language, voice, and opt-in gestures.
> L23: Heliox OS is an MIT-licensed, local-first desktop agent for Windows, macOS, and Linux. It translates typed or spoke
> L30: User intent → Planner → Permission and risk gates → Specialist → Executor → Verifier

## 星数曲线

```mermaid
xychart-beta
    title "VyomKulshrestha/Heliox-OS 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 66 --> 69
    line [67, 68, 68]
```

2026-10-18 67 → 2026-10-26 68（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `db94d36ef099` · [字段定义](../../DATASET.md)*

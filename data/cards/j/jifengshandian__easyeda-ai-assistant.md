# jifengshandian/easyeda-ai-assistant

⭐ 98 · TypeScript · Apache-2.0 · 推送 2026-03-13 · [GitHub](https://github.com/jifengshandian/easyeda-ai-assistant) · [官网](https://github.com/jifengshandian/easyeda-ai-assistant) · 个人维护 · 中文 README

**嘉立创 EDA Pro 原理图 AI 审查对话插件**

面向嘉立创 EDA 专业版用户的原理图审查助手扩展：自动采集原理图数据（器件、引脚、网络），解析 PROTEL NETLIST 2.0 网表并做引脚-网络绑定，以文字形式而非截图将电路细节提交 AI 分析；支持 13+ 家服务商的 reasoning 模型（OpenAI 兼容 API），提供流式对话、点击标签跳转元件、联网搜索数据手册、附件上传与 MCP 协议数据暴露（外部工具只读访问原理图）。自身不绘制原理图，只做检查。安装途径为立创开源广场、GitHub Releases 的 .eext 文件或源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网表驱动的引脚-网络绑定与悬空引脚检测（保守模式避免 NC 假阳性）
- 支持 13+ AI 服务商的 reasoning/thinking 模型，自动检测无需手动配置
- 点击对话中的蓝色标签（U1、VCC）直接定位到原理图元件
- 独立 MCP Server 通过 WebSocket 桥接，让 Cursor/Claude Code/Codex 等工具只读访问原理图数据（9 类 Resources、14 个 Tools）

## 适用场景

- 画完原理图后让 AI 检查电源、启动等电路问题
- 咨询芯片选型并联网搜索数据手册
- 让 Cursor/Claude Code 等外部 AI 工具读取原理图数据协同分析
- 排查调试问题（如 STM32 无法启动）时分析电路连接

## 场景标签

 · 领域:EDA/电子设计自动化

## 证据(README 行号)

> L11: 基于嘉立创 EDA 专业版的 AI 原理图对话助手，**不是帮你画图，而是帮你检查**！
> L24: - ✅ **以文字形式**完整理解你的原理图（器件、引脚、网络、连接关系）
> L92: - 🤖 **AI 对话助手** - 与 AI 对话，分析原理图设计

## 星数曲线

```mermaid
xychart-beta
    title "jifengshandian/easyeda-ai-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-28 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3ada5e037447` · [字段定义](../../DATASET.md)*

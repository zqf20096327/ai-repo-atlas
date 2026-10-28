# mohamed--abdel-maksoud/pisiguard

⭐ 22 · JavaScript · AGPL-3.0 · 推送 2026-08-03 · [GitHub](https://github.com/mohamed--abdel-maksoud/pisiguard) · 组织维护

**浏览器扩展：AI 聊天前自动脱敏个人信息并在回复中还原**

运行于浏览器本地的 Web 扩展：在消息发送到 AI 聊天平台前，识别姓名、邮箱、电话、信用卡号、密码、API 密钥等敏感信息，替换为唯一占位符，并在 AI 回复中自动还原原值。全部检测、遮蔽与还原在设备本地完成，不向外部服务发送数据、无遥测。支持 ChatGPT、Claude、DeepSeek 平台，可自定义检测规则。提供 Firefox 应用商店安装与 GitHub Releases 手动加载，也可用 pnpm 自行构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 发送前检测并遮蔽姓名/邮箱/电话/信用卡/密码/API 密钥等敏感信息
- AI 回复中自动还原原始值
- 全部处理在本地完成，无遥测、无服务器调用
- 支持自定义敏感信息检测规则

## 适用场景

- 在日常使用 AI 聊天时防止个人信息被发送到服务器
- 在 ChatGPT/Claude/DeepSeek 上讨论含敏感数据的问题时自动脱敏
- 按需扩展自己的敏感信息检测规则

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L11: I wanted something practical that will hide personal & sensitive data, and of course without routing them through y
> L22: - Works on popular AI chat platforms (ChatGPT, Claude, and DeepSeek).
> L23: - All processing stays on your device. No telemetry, no server calls, no analytics.

## 星数曲线

```mermaid
xychart-beta
    title "mohamed--abdel-maksoud/pisiguard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dfa378f3adf8` · [字段定义](../../DATASET.md)*

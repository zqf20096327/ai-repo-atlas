# houseworthe/claude-royale

⭐ 26 · Shell · MIT · 推送 2026-01-25 · [GitHub](https://github.com/houseworthe/claude-royale) · 个人维护

**让 AI agent 通过屏幕截图与点击自主玩 Clash Royale 的框架**

一个运行于 macOS 的 harness：通过屏幕截图、坐标映射与输入自动化，让 AI 系统自主操作 Clash Royale（经 BlueStacks 模拟器），用户负责提供 AI 决策部分。内置实现基于 Claude Code 的多 agent 架构：1 个 Commander 管理菜单与流程，3 个并行 Player agent 分摊出牌延迟。当前达到 1000+ 奖杯，曾在 Twitch 直播测试 12+ 小时。作者声明这是个人项目，坐标硬编码，未打包供一般使用，需自行重做坐标配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 屏幕截图+坐标映射+输入自动化的游戏接口层
- Commander + 3 并行 Player 的多 agent 架构，应对约 7 秒推理延迟
- 自动开局出牌、胜负按奖杯变化核验、结果屏检测与 agent 限制
- Twitch 直播集成与跨会话持久记忆

## 适用场景

- 观察多 agent 架构在实时游戏中的延迟应对方案
- 参考其屏幕捕获与坐标自动化方式构建类似游戏 agent
- 直播观看或复现 Claude 自主打 Clash Royale

## 场景标签

`多智能体` `GUI 自动化` · 领域:Agent 开发

## 证据(README 行号)

> L9: A harness for AI agents to play Clash Royale autonomously.
> L13: Claude Royale is an open framework that lets AI systems play Clash Royale through screen capture and input automati
> L15: The included implementation uses Claude Code with a multi-agent architecture: a Commander agent manages menus and g

## 星数曲线

```mermaid
xychart-beta
    title "houseworthe/claude-royale 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-31 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d285bcc53e9e` · [字段定义](../../DATASET.md)*

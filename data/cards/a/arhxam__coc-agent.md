# arhxam/coc-agent

⭐ 3 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/arhxam/coc-agent) · 个人维护

**在 Mac 上自动玩部落冲突的 Claude 代理**

基于 Claude Code computer use 与 macOS iPhone Mirroring 的自主游戏代理：通过截屏与点击操作 iPhone 上的部落冲突，无游戏 API、无内存读取、无注入代码。首次运行勘察账号后自建升级队列与进攻计划，内置六种策略配置文件；具有持久记忆、按统计自我调参、每日重写 strategy.md、每周回顾等机制。依赖 macOS 15+、Claude Code 订阅与 iPhone Mirroring（iOS 18+），Python 无第三方包。README 明确警告运行违反 Supercell 服务条款，账号可能被封禁。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯视觉操作：仅通过 iPhone Mirroring 看屏点击，无 API/注入
- 六种策略配置文件（max-out/fast-progress/war-ready 等）与自定义开关（如禁止花宝石）
- 持久记忆与自我改进：日志攻击、调参、每日重写 strategy.md
- 安全约束：PreToolUse 钩子仅允许操作 iPhone Mirroring，禁网络访问

## 适用场景

- 夜间挂机让代理自动打资源、保持建筑工人忙碌
- 按策略配置文件自动升级基地与城墙
- 研究 computer use 代理在真实 GUI 上的行为

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3:  An autonomous Clash of Clans agent built on Claude Code computer use and macOS iPhone Mirroring.
> L22: There's no game API, no memory reading and no injected code. Claude **looks at the screen and taps**, the way you w


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `741708f0c575` · [字段定义](../../DATASET.md)*

# cuddly-guacamole/opencode-routing-suite

⭐ 21 · JavaScript · NOASSERTION · 推送 2026-10-12 · [GitHub](https://github.com/cuddly-guacamole/opencode-routing-suite) · 个人维护 · 中文 README

**DeepSeek V4 专用任务路由套件：opencode 插件，四阶段渐进披露**

移植自 dsh-routing-suite 的 opencode 插件，面向 DeepSeek V4 模型做任务感知路由：standard agent 首轮将 system 替换为 RL 训练句，phase_begin 后按了解/对齐→拟合方案→开发→验证四阶段闯关，晋级由完成信号驱动；spec agent 则零干预深度思考。提供 tools_catalog/tools_help 二级披露、delivery_check 交付门（V2 可选阶段化门控，默认关）、阶段状态持久化与首条消息自动路由。非 DeepSeek V4 模型零干预。同时兼容 opencode V1/V2 双宿主线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四阶段完成信号驱动的渐进披露闯关（standard agent）
- delivery_check 交付门：文件存在性 + 四类证据清单全 PASS 才可交付
- V2 宿主可选阶段化门控（OPENCODE_ROUTER_GATE=1，只锁写入面）
- 一个 default 入口同时兼容 opencode V1/V2 双宿主线

## 适用场景

- DeepSeek V4 用户在 opencode 中按阶段推进开发任务
- 构建类任务自动路由到 react 循环、规划类路由到深度思考
- 用交付门禁强制验证产物有证据后再宣告完成

## 场景标签

`编码 Agent` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: DeepSeek V4 路由套件的 opencode 实现——**渐进披露游戏化时间线**：首轮 system 还原为
> L62: 重启 opencode，**Tab** 切到 `standard` 或 `spec` agent，调 `dev_router_status` 验证
> L71: - **非 DeepSeek V4**：全部零干预（不注入、不替换、不改写）。

## 星数曲线

```mermaid
xychart-beta
    title "cuddly-guacamole/opencode-routing-suite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `98db7746b690` · [字段定义](../../DATASET.md)*

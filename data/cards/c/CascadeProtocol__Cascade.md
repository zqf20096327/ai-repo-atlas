# CascadeProtocol/Cascade

⭐ 25 · TypeScript · MIT · 推送 2026-06-22 · [GitHub](https://github.com/CascadeProtocol/Cascade) · 组织维护

**Solana 跨 DEX 套利扫描器：Claude agent 评估并执行价差机会**

TypeScript/Bun 实现的自动化套利程序：每 3 秒并行拉取 Jupiter、Raydium、Orca、Meteora 四个 DEX 的报价，计算跨场所价差与路径，由 Claude agent 调用 simulate_path 与 arb_decision 两个工具模拟价格冲击、滑点后给出 EXECUTE/SKIP/MONITOR 决定。内置过期报价过滤、wash-quote 启发式与 gas 成本模型，默认 paper trading 模式，需配置 ANTHROPIC_API_KEY 与 HELIUS_API_KEY。

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

- 每 3 秒并行扫描 4 个 Solana DEX 的价差
- Claude agent 以 simulate_path/arb_decision 工具循环做执行决策
- 过期报价过滤、wash-quote 启发式与恒定乘积价格冲击模型
- 默认 paper trading，PAPER_TRADING=true 时不上链执行

## 适用场景

- 监控 Solana DEX 间价差并模拟套利路径收益
- 在纸面模式下测试 agent 驱动的套利决策流程
- 通过 BaseVenue 扩展接入新交易场所

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L8: Autonomous cross-venue arbitrage scanner for Solana. Monitors price spreads across four DEXes every 3 seconds and us
> L35: 4. **Agent evaluates** — Claude calls `simulate_path` to apply price impact + slippage, then issues `EXECUTE`, `SKI
> L40: The Claude agent has two tools per evaluation:

## 星数曲线

```mermaid
xychart-beta
    title "CascadeProtocol/Cascade 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e2a3d3e9bce3` · [字段定义](../../DATASET.md)*

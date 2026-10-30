# godagoo/slopcheck-deslop

⭐ 18 · TypeScript · MIT · 推送 2026-08-25 · [GitHub](https://github.com/godagoo/slopcheck-deslop) · 个人维护

**量化 AI 生成 TypeScript 结构性退化的静态分析工具**

基于论文 SlopCodeBench（arXiv:2603.24755）的 TypeScript 静态分析工具：以圈复杂度与 SLOC 计算 erosion 比值（仅统计 CC>10 的可调用体质量占比），支持 audit 测量、baseline 快照、delta 对比（退化则退出码 1），并提供 Claude Code Stop hook 在每轮工作后回报变化而非阻断。读取 .ts/.tsx，需 Bun 运行。附 ast-grep 规则包 ts-pack-v1 与一项预注册实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- erosion 指标：CC>10 可调用体的质量占比，复杂度主导、规模取平方根调制
- audit/baseline/delta CLI，delta 在退化上升时以退出码 1 结束
- Claude Code Stop hook：每轮后对比基线并回报，不阻断会话
- 自建 TypeScript 规则包 ts-pack-v1，结果标注 rulesVersion，cloneShare 单独报告

## 适用场景

- 度量 AI 编码代理产出的代码结构性退化趋势
- 在 Claude Code 工作流中每轮自动回报 erosion 变化
- CI 中以 delta 退出码拦截退化提交

## 场景标签

 · 领域:开发工具/代码质量

## 证据(README 行号)

> L10: `slopcheck` measures it. **Slop Check** finds the mess and gives it one honest number.
> L54: `hooks/erosion-check.ts` is a Claude Code Stop hook. After each turn of work it

## 星数曲线

```mermaid
xychart-beta
    title "godagoo/slopcheck-deslop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `c01e31be15f3` · [字段定义](../../DATASET.md)*

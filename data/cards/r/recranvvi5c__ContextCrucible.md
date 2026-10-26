# recranvvi5c/ContextCrucible

⭐ 213 · Rust · MIT · 推送 2026-10-21 · [GitHub](https://github.com/recranvvi5c/ContextCrucible) · [官网](https://pablog-7.github.io/ecommerce-kushi/) · 个人维护

**给编码 agent 的硬预算上下文编译器：扫描、打分、产出打包**

Rust 编写的 CLI 工具（crucible），从代码仓库生成受 token 硬预算约束的上下文包：确定性扫描剔除 vendor 目录/生成物/二进制文件，启发式 token 估算，四路加和打分（路径/查询频率/导入图/符号定义），规则式密钥检测（命中即隔离并脱敏），再以动态规划求解 0/1 背包在预算内选文件，输出拼接包与逐条解释收录/排除原因的 JSON manifest。无嵌入、无学习模型、无网络调用，输出跨平台字节级确定。面向给编码 agent 准备上下文的开发者；核心仅依赖 Rust stdlib，另附 TypeScript 可视化 explorer。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性扫描剔除 vendor/生成物/二进制文件
- 四路加和打分并保留分解供 manifest 解释
- 规则式密钥检测（AWS/PEM/JWT 等），命中文件隔离且密钥脱敏
- DP 精确求解 0/1 背包，硬预算重构后强制执行

## 适用场景

- 在固定 context 窗口内为编码 agent 挑选最相关文件
- 避免密钥/凭证被灌入上下文包
- 审计上下文包中每个文件为何被收录或排除

## 场景标签

 · 领域:LLM 工具链/上下文工程

## 证据(README 行号)

> L5:  A budget-aware context compiler for coding agents.
> L22: `contextcrucible` is that foundry. It is a single, dependency-free Rust binary

## 星数曲线

```mermaid
xychart-beta
    title "recranvvi5c/ContextCrucible 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-26"]
    y-axis "stars" 205 --> 214
    line [206, 212, 213]
```

2026-10-23 206 → 2026-10-26 213（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `d34b95cb55e0` · [字段定义](../../DATASET.md)*

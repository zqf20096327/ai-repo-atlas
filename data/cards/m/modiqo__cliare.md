# modiqo/cliare

⭐ 462 · Rust · Apache-2.0 · 推送 2026-08-02 · [GitHub](https://github.com/modiqo/cliare) · [官网](https://cliare.sh) · 组织维护

**CLI 的 agent 就绪度评测工具：探测命令面并生成索引与评分卡**

以黑盒方式对已发布的 CLI 二进制做运行时探测，记录证据、推断命令形态、检测副作用，输出命令索引（command-index.json）、问题清单、评分卡、单命令摘要、角色报告与 CI 工件。面向三类用户：CLI 维护者用于在 CI 中发现命令形态漂移与帮助覆盖缺口；安全审查者用于捕获看似安全命令的文件系统写入等未记录行为；agent harness 构建者用命令索引替代反复试错，降低 token 消耗。以 Rust 实现，提供 cargo 安装、预编译二进制安装脚本与 Nix/Devbox 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 黑盒探测 CLI 运行时行为，记录证据而非依赖静态文档
- 生成证据支撑的命令索引（路径/flags/前置条件/输出契约/置信度）
- 探测快照文件系统状态，报告安全命令的持久副作用
- 面向 maintainer/harness/security 三种角色的报告与 CI 工件

## 适用场景

- 发布前审计我的 CLI 对 agent 是否可用、哪里会卡住
- 给 agent harness 提供命令索引，避免反复 --help 和试错烧 token
- 安全审查发现 CLI 中未记录的文件写入与认证行为

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L15: CLIARE answers those questions by measuring the released CLI binary as a black box. It probes runtime behavior unde
> L148: CLIARE creates a measured command surface that harnesses can query before agents explore.

## 星数曲线

```mermaid
xychart-beta
    title "modiqo/cliare 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 461 --> 470
    line [469, 462, 462]
```

2026-10-18 469 → 2026-10-30 462（-7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `2242ec6473c8` · [字段定义](../../DATASET.md)*

# xyun92/trilane

⭐ 30 · Rust · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/xyun92/trilane) · [官网](https://github.com/xyun92/trilane) · 组织维护 · 中文 README

**面向授权灰盒测试的自主 AI 渗透测试与多 agent 安全审计工具**

以 Rust + Tauri 构建的桌面应用，把一句自然语言目标转化为分阶段审计流程：先构建攻击面图（路由/代码路径/认证边界），再按六条语义车道（身份认证、注入、入口/文件/SSRF、业务逻辑、配置/密钥/加密、边缘覆盖）并行审计，合并去重后输出带严重度、证据、payload 与代码路径的发现报告。提供 Safe 与 Lab 两种模式，Lab 模式授予更广的本地文件与命令执行权限，仅限被明确授权的目标。npm 包内置 macOS Apple Silicon 预构建应用，其他平台可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 攻击面图先于深度审计构建
- 六条语义车道并行审计后合并去重
- 发现报告含严重度、证据、payload 与代码路径
- Safe/Lab 双模式与运行转录归档（~/.trilane/transcripts）

## 适用场景

- 对自有或授权的 Web 应用/API 做灰盒渗透测试
- 内部代码库与训练应用的安全审计
- 在授权范围内的 bug bounty 目标上做自动化审计

## 场景标签

`网络安全` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Autonomous gray-box security auditing with visible lanes, attack-surface state, and evidence-backed findings.
> L20: TriLane turns one natural-language objective into a staged audit cockpit for authorized local labs, internal codeba
> L61: - Runs a six-lane semantic audit across identity/auth, injection/client-side sinks, ingress/files/SSRF, business lo

## 星数曲线

```mermaid
xychart-beta
    title "xyun92/trilane 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bc0be92df954` · [字段定义](../../DATASET.md)*

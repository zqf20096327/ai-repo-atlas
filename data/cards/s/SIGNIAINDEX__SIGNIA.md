# SIGNIAINDEX/SIGNIA

⭐ 128 · Rust · NOASSERTION · 推送 2026-03-29 · [GitHub](https://github.com/SIGNIAINDEX/SIGNIA) · [官网](https://signialab.org/) · 组织维护

**将真实世界结构编译为可验证链上制品的结构编译器**

SIGNIA 是面向 Solana 的结构编译器：读取 Git 仓库、数据集、规范、API schema、工作流或配置等输入，经插件推导类型化中间表示，输出三类规范化制品——Schema（结构模型）、Manifest（确定性输入与构建元数据）、Proof（哈希与 Merkle 根）。通过 BLAKE3 稳定哈希与规范化 JSON 实现同输入同字节的确定性，支持将 schema 哈希发布到 Solana 链上注册表并按版本解析。提供 Rust CLI、HTTP API、TypeScript/Python SDK 与 Next.js 控制台；另含基于文档训练的项目问答助手服务。README 声明项目处于活跃开发期，接口可能在稳定版前变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 输入→类型化 IR→Schema/Manifest/Proof 三类规范化制品
- BLAKE3 稳定哈希与 Merkle 证明实现确定性可验证输出
- Solana Anchor 链上注册表：发布与解析 schema 版本
- 沙箱化插件机制支持新增输入类型（repo/dataset/spec/api/workflow/config）

## 适用场景

- 将仓库、数据集或 API schema 的结构发布为链上可验证注册表
- 构建可复现的确定性制品流水线
- 通过 HTTP API 或 SDK 集成结构编译与证明校验

## 场景标签

 · 领域:区块链/开发者基础设施

## 证据(README 行号)

> L22: SIGNIA is a **structure compiler**: it reads an existing real-world structure (a Git repository, dataset, spec, API
> L29: The goal is not to copy execution logic on-chain. The goal is to make **structure** composable and auditable for on

## 星数曲线

```mermaid
xychart-beta
    title "SIGNIAINDEX/SIGNIA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 127 --> 129
    line [128, 128]
```

2026-10-18 128 → 2026-10-28 128（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `60fd4dbbe16a` · [字段定义](../../DATASET.md)*

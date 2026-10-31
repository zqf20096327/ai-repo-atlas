# kerberos-io/vault

⭐ 42 · 推送 2025-12-31 · [GitHub](https://github.com/kerberos-io/vault) · [官网](https://doc.kerberos.io/vault/first-things-first/) · 组织维护

**视频监控数据集中存储平台：自带存储后端，支撑机器学习扩展**

Kerberos.io 生态的存储组件：将 Kerberos Agent 的录像从本地磁盘集中到用户自选的对象存储（AWS S3、GCP、Azure Blob 或本地 Minio、Ceph），提供 API 用于开发自定义算法与应用，作为视频分析和机器学习方案的后端。支持 Docker 与 Kubernetes 两种安装方式，需 MongoDB 并建议创建索引。属于 Kerberos Enterprise Suite，可对接 Kerberos Hub SAAS 或私有部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BYOS：可配置云端或本地对象存储作为持久化后端
- 提供 API 用于构建移动应用、Web 应用与机器学习服务扩展
- 支持 Docker 与 Kubernetes 两种安装方式
- 可连接 Kerberos Hub SAAS 或私有化 Kerberos Hub 安装

## 适用场景

- 把多台摄像头的录像集中存储到自选对象存储
- 在统一存储后端上构建视频分析或机器学习应用
- 企业搭建可扩展的视频监控基础设施

## 场景标签

 · 领域:视频监控/存储基础设施

## 证据(README 行号)

> L59: In addition to storing recordings in your Kerberos Agents, you have the option to Bring Your Own Storage (BYOS), us
> L61: Despite the flexible storage capabilities, Kerberos Vault is also an open platform, which can be used to build exte

## 星数曲线

```mermaid
xychart-beta
    title "kerberos-io/vault 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `9a9e72d21d04` · [字段定义](../../DATASET.md)*

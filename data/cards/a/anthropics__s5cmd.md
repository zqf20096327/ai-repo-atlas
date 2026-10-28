# anthropics/s5cmd

⭐ 44 · Go · MIT · 推送 2026-05-19 · [GitHub](https://github.com/anthropics/s5cmd) · 组织维护

**Anthropic 维护的 s5cmd 分支：S3/对象存储命令行工具，新增 GCS 与 WIF 支持**

Anthropic 对 peak/s5cmd 的 fork，目的是加入 Google Cloud Storage 支持与 Workload Identity Federation（WIF），使其无需长期凭证（HMAC 密钥）即可使用。本体是 S3 与本地文件系统的命令行执行工具，支持上传、下载、复制、删除、通配符、批量命令文件、stdin 管道上传等大量操作，使用官方 AWS SDK 签名。以 Go 编写，提供预编译二进制、Homebrew、Docker 与源码构建等安装方式；README 大部分沿用原项目文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在上游 s5cmd 基础上新增 GCS 与 WIF（Workload Identity Federation）支持
- 支持通配符、并行传输、批量命令文件（s5cmd run）
- 支持 stdin 管道上传、S3 服务端复制、--include/--exclude 过滤
- 通过官方 AWS SDK 签名，支持 EC2/EKS IAM 角色与匿名访问

## 适用场景

- 需要免长期凭证（HMAC key）操作对象存储的场景
- 大批量 S3 对象上传、下载与批量删除
- 从 stdin 流式管道上传数据到 S3

## 场景标签

 · 领域:云存储/开发者工具

## 证据(README 行号)

> L3: We have forked s5cmd in order to add GCS and WIF support so that we can continue
> L47: `s5cmd` is a very fast S3 and local filesystem execution tool. It comes with support

## 星数曲线

```mermaid
xychart-beta
    title "anthropics/s5cmd 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-28 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a0b2cd7e8587` · [字段定义](../../DATASET.md)*

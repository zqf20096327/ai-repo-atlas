# synpse-hq/synpse

⭐ 21 · Apache-2.0 · 推送 2026-06-06 · [GitHub](https://github.com/synpse-hq/synpse) · [官网](https://synpse.com) · 组织维护

**服务器与 IoT 设备集群管理平台：声明式部署、SSH 隧道与 OTA 更新**

设备与应用编排工具：设备注册后可通过 UI/CLI 查看，支持基于隧道的 SSH/TCP 访问（设备无需公网 IP）、从 GitHub/Gitlab 等仓库读取清单的声明式应用部署、基于标签与选择器的设备分组调度、加密密钥存储与命名空间隔离。平台支持 Linux（amd64/aarch64/arm32），Darwin 需自行以守护进程方式安装 agent，Windows 支持列为计划项。README 未提及 AI 相关功能，仓库主题标签含 ai/machine-learning 但正文无对应说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备清单管理与 UI/CLI 仪表盘
- 通过隧道的 SSH/TCP 访问，设备无需公网 IP
- 声明式应用部署与基于标签的设备调度
- 加密密钥存储与命名空间隔离

## 适用场景

- 管理分散的服务器或 IoT 设备集群并做 OTA 更新
- 给无公网 IP 的设备建立 SSH/TCP 远程访问
- 用声明式清单向设备子集部署应用（如 A/B 测试）

## 场景标签

 · 领域:DevOps/设备编排

## 证据(README 行号)

> L18: - Device inventory management: each of your device will register as an entry in our database and will be visible vi
> L19: - SSH/TCP connections to your devices via tunnels: you don't need to have a public IP on your device to have access
> L20: - Declarative application deployment: store your manifests in GitHub, Gitlab or any other SCM repository, deploy ap

## 星数曲线

```mermaid
xychart-beta
    title "synpse-hq/synpse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `1fa3c4c545cf` · [字段定义](../../DATASET.md)*

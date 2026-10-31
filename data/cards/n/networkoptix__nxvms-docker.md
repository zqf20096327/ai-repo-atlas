# networkoptix/nxvms-docker

⭐ 16 · Dockerfile · 推送 2026-07-28 · [GitHub](https://github.com/networkoptix/nxvms-docker) · [官网](https://networkoptix.com) · 组织维护

**Nx Meta 视频管理平台的官方 Docker 部署方案**

由 Network Optix 提供的容器化部署包，通过 Docker Compose 启动 Nx Meta 及 Powered-by-Nx 视频管理产品。默认以 docker-compose.yaml 编排各组件，README 声明该配置即其 QA 团队的官方测试标准，且版本锁定。限制：仅支持 Debian Linux 容器，Linux 主机支持，macOS 主机有限制，Windows 主机未测试；容器内运行 Nx Server 属实验特性，不建议用于关键系统。许可证与硬件 ID（HWID）绑定，网络或容器改动会使许可证失效，可联系支持最多重新激活 3 次。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Docker Compose 一键编排 Nx Meta 各组件，版本锁定并经官方 QA 验证
- 预构建镜像发布于 Nx registry，也支持本地 docker-compose build
- 明确列出视频存储卷挂载点与支持的文件系统类型（ext4/xfs/nfs/cifs 等）
- 文档说明 HWID 与许可证失效场景及最多 3 次重激活规则

## 适用场景

- 在 Linux 服务器上以容器方式部署 Nx Meta 视频管理系统
- 复现与官方 QA 环境一致的标准化部署
- 为已有传统方式安装的 VMS 服务器并行运行容器实例（需调整端口）

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: ## Abstract ##
> L27: * Nx Server Docker container is an experimental feature.

## 星数曲线

```mermaid
xychart-beta
    title "networkoptix/nxvms-docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `21e67970c023` · [字段定义](../../DATASET.md)*

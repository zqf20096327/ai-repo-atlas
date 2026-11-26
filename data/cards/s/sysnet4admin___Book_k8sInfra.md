# sysnet4admin/_Book_k8sInfra

⭐ 502 · Shell · 推送 2026-11-24 · [GitHub](https://github.com/sysnet4admin/_Book_k8sInfra) · [官网](https://product.kyobobook.co.kr/detail/S000221973541) · 组织维护

**Kubernetes/Docker 教材书的配套实练代码仓库**

韩国出版的《为现代开发者的 Kubernetes/Docker》一书的配套实练代码。提供按章节组织的 Vagrantfile、配置脚本与 YAML 清单，指导读者用 Vagrant 虚拟机自建 Kubernetes 集群，依次实练 Docker 与 Harbor、Jenkins CI/CD、Prometheus/Grafana 监控套件；第 7 章涵盖 Operator 模式、OpenTelemetry、Argo CD/Rollouts 与小型 LLM。另提供 OVA 镜像（OneDrive 下载）替代 Vagrant 构建环境，附带勘误表与配套视频链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按章节组织的实练代码：集群搭建、镜像构建、CI/CD、监控套件
- 提供 OVA 镜像（arm64/x86）直接导入 VirtualBox 跳过 Vagrant 构建环境
- 第 7 章包含 Argo CD/Rollouts、Cilium 网络策略与小型 LLM 实练
- rerepo-book-k8sinfra 命令一键还原实练文件

## 适用场景

- 跟随书籍章节从零搭建并实练 Kubernetes 集群
- 用 GitOps（Argo）与 Jenkins 实练持续集成部署流程
- 快速用 OVA 镜像获得现成的多节点实验环境

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L23: 이 저장소는 요즘 개발자를 위한 쿠버네티스/도커 책의 실습을 위한 코드를 제공합니다.
> L25: 베이그런트로 만든 가상 머신 위에 쿠버네티스 클러스터를 직접 구성하고, 도커와 하버, 젠킨스, 프로메테우스와 그라파나 제품군을 실습합니다. 7장에서는 오퍼레이터 패턴, 오픈텔레메트리, 아르고 CD와 아르고 

## 星数曲线

```mermaid
xychart-beta
    title "sysnet4admin/_Book_k8sInfra 星数(近 2 点)"
    x-axis ["2026-11-21", "2026-11-26"]
    y-axis "stars" 501 --> 503
    line [502, 502]
```

2026-11-21 502 → 2026-11-26 502（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `9cb7c5564508` · [字段定义](../../DATASET.md)*

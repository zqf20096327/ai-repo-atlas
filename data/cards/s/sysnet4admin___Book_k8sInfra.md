# sysnet4admin/_Book_k8sInfra

⭐ 502 · Shell · 推送 2026-11-24 · [GitHub](https://github.com/sysnet4admin/_Book_k8sInfra) · [官网](https://product.kyobobook.co.kr/detail/S000221973541) · 组织维护

**Kubernetes/Docker 图书配套实验代码仓库：供读者搭建集群练习**

韩国图书《요즘 개발자를 위한 쿠버네티스/도커》的配套代码仓库，提供章节实验文件：用 Vagrant 创建虚拟机构建 Kubernetes 集群，依次练习 Docker、Harbor、Jenkins、Prometheus/Grafana 监控栈，第 7 章覆盖 Operator 模式、OpenTelemetry、Argo CD/ rollouts、Cilium 网络策略及小型 LLM。除 Vagrantfile 路径外还提供 OVA 预建镜像（4 台虚拟机，分 arm64/x86），并附勘误表、参考文档与教学视频链接。

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

- 按章节组织的 Kubernetes/Docker/GitOps 实验代码（ch2–ch7 及附录）
- 提供 OVA 预建镜像替代 Vagrant，证书有效期至 2036 年 11 月
- 一条 rerepo 命令恢复实验代码初始状态
- 含 kubespray 多控制面集群、runC 容器深入等附录实验

## 适用场景

- 跟着图书章节搭建本地 Kubernetes 学习集群
- 练习 GitOps、CI/CD（Jenkins、Argo CD/rollouts）流程
- 用 OVA 镜像快速获得可用的多节点实验环境

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L23: 이 저장소는 요즘 개발자를 위한 쿠버네티스/도커 책의 실습을 위한 코드를 제공합니다.
> L25: 베이그런트로 만든 가상 머신 위에 쿠버네티스 클러스터를 직접 구성하고, 도커와 하버, 젠킨스, 프로메테우스와 그라파나 제품군을 실습합니다. 7장에서는 오퍼레이터 패턴, 오픈텔레메트리, 아르고 CD와 아르고 
> L31: |ch2|<small>테스트 환경 구성하기</small>|<small>가상 머신을 만드는 Vagrantfile과 프로비저닝 스크립트, macOS용 버추얼박스, 베이그런트, 타비 설치 파일</small>|

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
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `4d4068f6ce9b` · [字段定义](../../DATASET.md)*

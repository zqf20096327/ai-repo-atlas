# KhaiTrang1995/llm-internal

⭐ 19 · HTML · NOASSERTION · 推送 2026-08-16 · [GitHub](https://github.com/KhaiTrang1995/llm-internal) · [官网](https://khaitrang1995.github.io/llm-internal/) · 个人维护

**自托管 LLM 推理集群 MLOps 双语案例研究文档**

一份面向社区开放的运维案例研究（文档仓库，不含 compose 文件），记录以 vLLM 为 serving 引擎、LiteLLM 做网关、Portainer CE 做 GitOps 控制面、Netdata 做观测的自托管 LLM 集群架构。内容覆盖请求链路、分层设计、需关注的 vLLM 指标（TTFT、KV cache 等）、六条运维经验、MLOps 检查清单及架构适用边界（1–2 GPU 节点规模）。参考环境为 Ubuntu 22.04/24.04、NVIDIA Ampere 及以上 GPU、驱动 ≥550。越文/英文双语，完整部署指南以越文撰写。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- vLLM + LiteLLM + Portainer CE + Netdata 的分层架构与请求/运维双链路描述
- Netdata 经 go.d/prometheus collector 同时采集基础设施与 vllm:* 应用指标
- 六条运维经验与配置/可靠性/安全/观测四类 MLOps 检查清单
- 明确声明架构边界：1–2 GPU 节点规模、无 autoscaling、Netdata 替代 Prometheus/Grafana 仅限小规模

## 适用场景

- 搭建公司内部自托管 LLM 推理集群前参考架构与检查清单
- 了解 vLLM 关键指标（TTFT、KV cache、队列）的监控与告警配置
- 学习 GitOps 方式通过 Portainer 部署与换模

## 场景标签

`LLM 可观测性` `MLOps` · 领域:评测与运维

## 证据(README 行号)

> L3: **Chạy LLM nội bộ theo chuẩn MLOps — case study mở cho cộng đồng**
> L21: Chạy được một model thì dễ — `docker run` là xong trong mười phút. Cái khó nằm ở phần còn lại: làm sao biết model đ
> L81: > Ba file `*-stack.yml` dưới đây là **file bạn tự tạo** bằng cách copy compose từ hướng dẫn — repo này là tài liệu,

## 星数曲线

```mermaid
xychart-beta
    title "KhaiTrang1995/llm-internal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `a1257e6c97bf` · [字段定义](../../DATASET.md)*

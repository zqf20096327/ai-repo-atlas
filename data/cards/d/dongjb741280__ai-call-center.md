# dongjb741280/ai-call-center

⭐ 114 · Java · GPL-3.0 · 推送 2026-11-19 · [GitHub](https://github.com/dongjb741280/ai-call-center) · [官网](https://dongjb741280.github.io/ai-call-center/) · 个人维护 · 中文 README

**企业客服与外呼业务的开源呼叫中心系统**

基于 FreeSWITCH、Spring Boot 与 Vue 3 的开源呼叫中心，采用微服务架构（Nacos、Spring Cloud），提供多租户、ACD 技能组路由（最少接听/最长空闲/轮询等 6 种策略）、VDN/IVR 流程引擎、智能外呼任务调度、WebRTC/SIP 坐席软电话与录音管理（Nginx 服务录音文件并上传 MinIO）。README 声明主要面向大规模人工呼入呼出场景，也可作为 AI 语音应用的呼叫底座；纯无人值守 AI 外呼由同作者的另一项目承接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ACD 路由支持 6 种分配策略与 VIP 队列、溢出处理
- IVR 引擎解析工作流定义为节点图并执行播放/收号/转接
- 外呼任务引擎支持巡航/预测式节奏控制与租约恢复
- 录音经 Nginx 回传并上传 MinIO，支持 Excel 报表导出

## 适用场景

- 搭建企业多租户客服呼叫中心
- 管理人工坐席的呼入呼出与技能组排班
- 执行批量外呼任务并导出通话统计报表
- 为 AI 语音应用提供呼叫接入底座

## 场景标签

 · 领域:企业通信/呼叫中心

## 证据(README 行号)

> L3: 基于 FreeSWITCH、Spring Boot 和 Vue 3 的开源呼叫中心系统，支持多租户、人工呼入呼出、智能外呼任务、ACD 技能组路由、IVR、WebRTC 坐席与录音管理，适用于企业客服和外呼业务，也可作为 AI 语音
> L23: > This project is primarily intended for large-scale human inbound and outbound calling scenarios, or as the founda

## 星数曲线

```mermaid
xychart-beta
    title "dongjb741280/ai-call-center 星数(近 9 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-18", "2026-11-28"]
    y-axis "stars" 0 --> 124
    line [10, 23, 26, 93, 100, 101, 100, 113, 114]
```

2026-11-08 10 → 2026-11-28 114（+104）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `a6cce3238510` · [字段定义](../../DATASET.md)*

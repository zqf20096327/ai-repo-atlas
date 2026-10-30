# RattyDAVE/docker-jupyterhub

⭐ 19 · Python · 推送 2026-10-29 · [GitHub](https://github.com/RattyDAVE/docker-jupyterhub) · 个人维护

**多用户 JupyterHub Docker 镜像：预装 C++/Java/Python/TensorFlow 等多语言环境**

基于 Docker 的 JupyterHub 多用户笔记本服务镜像：通过 createusers.txt 文件批量创建 Linux 用户并授予 sudo 权限，重启时自动追加新用户；容器内预装 C++（xeus-cling）、Node.js、Clojure、Groovy、Java、Kotlin、Scala、SQL、Python 等多语言内核，并包含 TensorFlow、PyTorch 及 BeakerX 扩展、示例与教程。部署方式为 docker run，可配合 watchtower 自动更新、nginx-proxy 与 letsencrypt 组件添加 SSL。面向需要向学生、研究人员、数据科学团队共享计算环境的管理者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- createusers.txt 批量创建用户并支持 sudo 权限分配，重启自动追加新用户
- 预装多语言 Jupyter 内核：C++/Java/Clojure/Groovy/Kotlin/Scala/SQL/Node.js 等
- 内置 TensorFlow 与 PyTorch 及完整入门到进阶教程
- 可通过 watchtower 自动更新，nginx-proxy + letsencrypt 添加 SSL

## 适用场景

- 为课程或团队快速部署多用户 JupyterHub 环境
- 让学生或研究人员免安装即可使用多语言数据科学环境
- 在内网或公网上以 SSL 方式共享预配置计算资源

## 场景标签

 · 领域:数据科学/开发环境

## 证据(README 行号)

> L5: JupyterHub brings the power of notebooks to groups of users. It gives users access to computational environments and
> L18: docker run -d  --restart unless-stopped \

## 星数曲线

```mermaid
xychart-beta
    title "RattyDAVE/docker-jupyterhub 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-25 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a4f3bbde3f85` · [字段定义](../../DATASET.md)*

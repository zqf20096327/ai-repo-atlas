# olasupo/bubbln_network-automation

⭐ 38 · Python · GPL-3.0 · 推送 2026-04-17 · [GitHub](https://github.com/olasupo/bubbln_network-automation) · [官网](http://www.bubbln.com) · 个人维护

**用 ChatGPT 生成并执行 OSPF/EIGRP 网络 Ansible 剧本的工具**

面向网络工程师的 Python 工具，充当 ChatGPT 与网络设备之间的桥梁：用户输入路由器参数（OSPF/EIGRP、接口、CIDR 地址等），工具将其与预置自然语言指令组合成提示词发送给 ChatGPT（gpt-4，temperature 0.2），从回复中提取 Ansible 剧本，并用 ansible_runner 自动生成 hosts.yml 并在 SSH 可达的路由器上执行。已测试场景限于 OSPF 与 EIGRP 网络；需 OpenAI API Key 与可 SSH 的路由器环境。提供 Docker 镜像与源码克隆两种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ChatGPT 自动生成 OSPF/EIGRP 的 Ansible playbook 并经 ansible_runner 执行
- 由 SSH IP 列表与登录凭据自动生成 hosts.yml inventory 文件
- 参数输入含数据类型/CIDR 格式校验与用户确认环节
- 自动生成含配置、提示词与剧本的报告文档

## 适用场景

- 我想让 AI 代替手写 Ansible 剧本来配置 OSPF/EIGRP 网络
- 在实验环境（如虚拟化路由器）中快速部署网络配置
- 自动留档网络配置与生成剧本以备查阅

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L9: And that's why we built Bubbln. It's a game-changer in network engineering, integrating AI into Ansible to take auto
> L13: **AI-Driven Playbook Generation for OSPF and EIGRP based networks:** Bubbln has been rigorously tested to leverage 

## 星数曲线

```mermaid
xychart-beta
    title "olasupo/bubbln_network-automation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f53abf9ef414` · [字段定义](../../DATASET.md)*

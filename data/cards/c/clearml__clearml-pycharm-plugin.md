# clearml/clearml-pycharm-plugin

⭐ 36 · Java · Apache-2.0 · 推送 2026-03-12 · [GitHub](https://github.com/clearml/clearml-pycharm-plugin) · [官网](https://clear.ml/docs/latest/docs/guides/ide/integration_pycharm) · 组织维护

**将本地执行配置同步到远程调试机的 PyCharm 插件**

ClearML 出品的 PyCharm 插件：把本地仓库信息同步到远程执行/调试机，支持多用户共用同一执行资源而不暴露私有凭据，并可在默认 VM/容器上运行 ClearML Agent。安装方式为从 Releases 页面下载插件文件后从本地磁盘安装到 PyCharm。插件内可配置 ClearML 服务器地址（API/Web/File server）与用户密钥，该配置会覆盖 ClearML 配置文件中的对应设置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同步本地仓库信息到远程调试机
- 多用户共用执行资源且不暴露私有凭据
- 可在默认 VM/容器上运行 ClearML Agent
- 插件内配置 ClearML 服务器与凭据（覆盖配置文件）

## 适用场景

- 在 PyCharm 中把本地代码同步到远程机器调试运行
- 团队多人共用远程执行资源并隔离各自凭据
- 通过 IDE 配置 ClearML 服务器连接信息

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L6: The **ClearML PyCharm plugin** enables syncing local execution configuration to a remote executor machine:
> L12: * Run the ClearML Agent on default VMs/Containers.

## 星数曲线

```mermaid
xychart-beta
    title "clearml/clearml-pycharm-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a58334562776` · [字段定义](../../DATASET.md)*

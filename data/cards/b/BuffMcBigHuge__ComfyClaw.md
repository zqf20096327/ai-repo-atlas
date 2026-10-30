# BuffMcBigHuge/ComfyClaw

⭐ 18 · JavaScript · MIT · 推送 2026-08-23 · [GitHub](https://github.com/BuffMcBigHuge/ComfyClaw) · 个人维护

**ComfyUI 工作流的发现、检查与执行 CLI，供 LLM/脚本自动化调用**

面向 ComfyUI 用户的命令行工具：列出 workflows/ 目录下的工作流，通过 @tag 系统定位节点并以 --set/--file/--mode/--switch 覆盖参数，经服务器前端编译 UI 工作流生成 API 请求，经 /prompt 队列执行并下载输出。支持 --check 对 /object_info 校验覆盖项、--diff-ui 对比 UI 与 API 图差异、--inventory 从服务器或本地目录盘点模型资产。可选将输出上传 AWS S3，默认关闭。设计目标为 LLM 或脚本无需读取工作流 JSON 即可自动化操作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- @tag 标签系统定位节点，参数覆盖不触及已连线的图接线
- 通过服务器前端（含自定义扩展）编译 UI 工作流生成 API 请求
- --inventory 从 /object_info 或本地目录扫描盘点 checkpoint/LoRA/VAE 等资产
- 可选输出自动上传 AWS S3（默认关闭）

## 适用场景

- 用脚本或 LLM 自动化执行 ComfyUI 图像/视频生成工作流
- 批量调整提示词、采样参数并校验覆盖项合法性
- 盘点本地或服务器上的模型与 LoRA 资产

## 场景标签

`工作流自动化` `图像生成` `视频生成` · 领域:效率与自动化

## 证据(README 行号)

> L5: A CLI for discovering, inspecting, and running ComfyUI workflows — with **tag-based parameter overrides** and **serv
> L7: > **Designed for automation.** An LLM or script can discover workflows, inspect editable parameters, and execute the

## 星数曲线

```mermaid
xychart-beta
    title "BuffMcBigHuge/ComfyClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `641624578b9f` · [字段定义](../../DATASET.md)*

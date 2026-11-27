# yangyi-student/zhidao-helper

⭐ 3 · Python · GPL-3.0 · 推送 2026-11-07 · [GitHub](https://github.com/yangyi-student/zhidao-helper) · 个人维护 · 中文 README

**知到（智慧树）网课自动化学习助手，含答题与刷课**

面向知到（智慧树）共享课的 Python 自动化工具，提供扫码登录、视频进度上报、弹窗/作业/考试自动作答。答案策略为本地缓存→LLM 生成→随机兜底三级，LLM 走任意 OpenAI 兼容接口。提供 Typer CLI 与 Tkinter GUI 双入口，支持 SOCKS5 代理与日志脱敏。README 明确声明为非官方工具，使用可能违反学术诚信规范，作业/考试功能必须配置 API Key 否则降级为缓存/随机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三级答案策略：缓存命中→LLM 生成→随机兜底，SQLite 双键缓存跨 exam 复用
- Typer CLI + Tkinter GUI 双入口，Windows 可打包单文件 exe
- V2 心跳视频进度上报与随机暂停、WatchPoint 轨迹复现
- 日志自动脱敏 api_key/token，按天轮转保留 30 天

## 适用场景

- 自动化完成知到共享课视频学时进度
- 配置 LLM API Key 后自动作答作业与考试
- 导出/导入题库缓存，在课程内复用答案

## 场景标签

 · 领域:教育/自动化工具

## 证据(README 行号)

> L5:  知到（智慧树）共享课的自动化学习工具
> L44: |**三级答案策略**|本地缓存命中 → LLM 生成（带排除错误项 / 历史解析 / 题库参考）→ 随机兜底|
> L62: |LLM|openai SDK（OpenAI 兼容接口）|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `55385253e19a` · [字段定义](../../DATASET.md)*
